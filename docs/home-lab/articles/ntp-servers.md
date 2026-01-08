---
title: NTP Servers
date: 2023-10-10
description: Setting up a local NTP server with Chrony for accurate timekeeping.
image: https://via.placeholder.com/300x200?text=NTP
---

# 1. Install Chrony & Stop the old time service
sudo apt-get update
sudo apt-get install chrony -y
sudo systemctl stop systemd-timesyncd
sudo systemctl disable systemd-timesyncd
sudo systemctl enable chrony

# 2. Write the "Boot Proof" Config
sudo bash -c 'cat > /etc/chrony/chrony.conf <<EOF
# --- BOOT PROOF NTP SERVERS (IPs) ---
# Google Public NTP (IPs solve the "1970" boot loop)
server 216.239.35.0 iburst
server 216.239.35.4 iburst

# Cloudflare Public NTP
server 162.159.200.1 iburst
server 162.159.200.123 iburst

# --- OFFICIAL FINNISH AUTHORITIES ---
# VTT MIKES
server time.mikes.fi iburst
server time1.mikes.fi iburst
server time2.mikes.fi iburst

# DNA & FUNET
server ntp.dnainternet.fi iburst
server ntp.funet.fi iburst

# --- CORE SETTINGS ---
driftfile /var/lib/chrony/chrony.drift
makestep 1.0 3
rtcsync

# --- ACCESS CONTROL ---
# Allow local network to sync from this server
allow 10.0.0.0/8

# Listen on all interfaces
bindcmdaddress 0.0.0.0

# --- LOGGING ---
logdir /var/log/chrony
EOF'

# 3. Restart Chrony to apply
sudo systemctl restart chrony

# verify the sources
chronyc sources -v