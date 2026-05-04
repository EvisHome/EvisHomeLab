# File: /mnt/docker/appdata/ai-reporter/reporter.py

import os
import requests
import datetime
import time
from google import genai
from collections import defaultdict

# --- CONFIGURATION ---
LOKI_URL = os.getenv("LOKI_URL", "http://localhost:3100")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
HA_URL = os.getenv("HA_URL")
HA_TOKEN = os.getenv("HA_TOKEN")

def get_source_name(labels):
    """
    Standardized naming for the AI:
    - If it's a container: 'unraid/plex'
    - If it's a system log: 'unraid/syslog' or 'UDM-Pro/unifi'
    """
    host = labels.get('host', 'unknown')
    job = labels.get('job', 'unknown')
    container = labels.get('container_name', '')

    if container:
        return f"{host}/{container}"
    return f"{host}/{job}"

def get_loki_logs():
    """Fetches logs for the last 24h and deduplicates them."""
    total_duration_hours = 24
    chunk_size_hours = 6 # Fetch in chunks to avoid timeouts
    current_time = time.time()

    # Query: Find errors/warnings, exclude chatty noise
    query = '{job=~".+"} != "promtail" != "docker-socket-proxy" |~ "(?i)error|warn|fail|exception|timeout|blocked|detected|critical|panic" !~ "(?i)info|debug"'

    unique_events = defaultdict(lambda: defaultdict(int))
    total_lines = 0

    print(f"Analyzing logs for the last {total_duration_hours} hours...")

    for i in range(0, total_duration_hours, chunk_size_hours):
        chunk_end = int((current_time - (i * 3600)) * 1e9)
        chunk_start = int((current_time - ((i + chunk_size_hours) * 3600)) * 1e9)

        params = {'query': query, 'limit': 5000, 'start': chunk_start, 'end': chunk_end, 'direction': 'backward'}

        try:
            r = requests.get(f"{LOKI_URL}/loki/api/v1/query_range", params=params, timeout=30)
            if r.status_code != 200: continue
            data = r.json()

            for stream in data.get('data', {}).get('result', []):
                source = get_source_name(stream.get('metric', {}))
                for entry in stream['values']:
                    log_line = entry[1].strip()[:500] # Get first 500 chars of log
                    unique_events[source][log_line] += 1
                    total_lines += 1
        except Exception as e:
            print(f"Error fetching chunk: {e}")

    if not unique_events:
        return "No critical errors or security events found in the last 24 hours."

    # Format the findings for the AI
    report_data = []
    for source, messages in unique_events.items():
        for msg, count in messages.items():
            line = f"[{source}] {msg}"
            if count > 1:
                line += f" (Seen {count} times)"
            report_data.append(line)

    print(f"Compressed {total_lines} lines into {len(report_data)} unique event types.")
    return "\n".join(report_data)

def summarize_with_gemini(logs):
    if "No critical errors" in logs:
        return logs

    client = genai.Client(api_key=GEMINI_API_KEY)

    prompt = (
        "You are a Senior Site Reliability Engineer. Analyze these home lab logs.\n"
        "1. Group by priority: 🔴 CRITICAL, 🛡️ SECURITY, 🟡 WARNING.\n"
        "2. Focus on high repetition counts (Seen X times).\n"
        "3. Ignore noise; be extremely concise and actionable.\n\n"
        f"LOG DATA:\n{logs[:90000]}"
    )

    try:
        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        return response.text
    except Exception as e:
        return f"Gemini API Error: {str(e)}"

def post_to_ha(summary):
    if not HA_TOKEN: return
    headers = {"Authorization": f"Bearer {HA_TOKEN}", "Content-Type": "application/json"}

    # Send Notification
    requests.post(f"{HA_URL}/api/services/persistent_notification/create", headers=headers, json={
        "message": summary,
        "title": f"🤖 Daily Lab Report ({datetime.datetime.now().strftime('%H:%M')})",
        "notification_id": "daily_ai_summary"
    })

    # Update Dashboard Sensor
    requests.post(f"{HA_URL}/api/states/sensor.daily_system_summary", headers=headers, json={
        "state": datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
        "attributes": {
            "summary": summary,
            "friendly_name": "Daily System Summary",
            "icon": "mdi:robot"
        }
    })

if __name__ == "__main__":
    logs = get_loki_logs()
    summary = summarize_with_gemini(logs)
    post_to_ha(summary)
    print("Done. Report sent to Home Assistant.")