---
title: Zigbee Network / Sonoff ZBDongle-E
date: 2026-01-17
description: Build a custom wall mount for your Philips Hue motion sensor.
image: ambilight-2012-2022/ambilight.jpg
draft: true
highlight: false
tags:
  - zigbee
  - sonoff
  - zbdongle-e
---

# Zigbee Network / Sonoff ZBDongle-E

This focuses more on the Sonoff ZBDongle-E and how to use it to create a Zigbee network, and fix problems I run into.

My Zigbee network is currently experiencing a lot of "buffer overflow" and "Broadcast Failed", and I am

<br/>

## Solutions

* Flashing the firmware (with Hardware Flow Control)
* Using a USB extension cable to connect the ZBDongle-E to my Raspberry Pi running Zigbee2MQTT
* Enabling the Hardware Flow Control
* Increasing the baudrate from 115200 to 460800
* "Hard Mesh Reser"

```YAML
serial:
  port: /dev/ttyACM0
  adapter: ember
  baudrate: 460800  # Matches the firmware you just flashed
  rtscts: true      # Enables the Hardware Flow Control
```

<br/>

## Hard Mesh Reset

Because Zigbee routers (lights and switches) cache routing paths, a simple software restart won't clear a stuck broadcast queue. You need to force the entire mesh to forget the deadlocked paths.

1. Stop the Zigbee2MQTT container.
2. Unplug the Zigbee Coordinator from the Pi.
3. Kill the power to your Zigbee Routers: Turn off the circuit breakers for your Kitchen, Bathroom, and Bedroom lights for at least 30 seconds.
4. Plug the Coordinator back in (Ensure it is on a USB 2.0 extension cable).
5. Start Zigbee2MQTT.
6. Restore power to the lights.

This forces every device to re-announce itself and rebuild the routing table from scratch.

<br/>

## Flashing the firmware

* Download the latest firmware from the [Sonoff ZBDongle-E](https://sonoff.tech/sonoff-zbdongle-e/)
* Flash the firmware using the [Sonoff ZBDongle-E](https://sonoff.tech/sonoff-zbdongle-e/)

Firmware: Ensure you are running EmberZNet 7.4.x or newer. If your firmware is from 2024 or earlier, it may have a bug regarding buffer management that was fixed in late 2025.

<br/>

## Raspberry Pi 5 USB ports

Your setup (RPi 5 + long extension cable) is perfect, but there is one final trick:

Use the USB 2.0 (Black) ports on the Pi 5.

The Blue (USB 3.0) ports on the Pi 5 generate a massive amount of 2.4GHz noise right at the port, which can travel down the shielding of even a long cable. Using the black port removes this interference entirely.



## Chatty Devices Fooling the Coordinator

* Aqara W500
* Washing Machine plug

absolutely flooding your network

The "Spam" Analysis
Look at the timestamps:

Aqara W500: It is sending double updates (sometimes two at the exact same second: 9:16:49, 9:16:55, 9:16:59). In just 30 seconds, it sent over 12 massive JSON payloads.

Washing Machine Plug: It is reporting tiny power fluctuations (0.2 to 0.3 watts) every few seconds.

### Throttle the Aqara W500
Aqara devices are notorious for "double-reporting." We can fix this in the Z2M Frontend or configuration.yaml.

* Frontend: Go to the device Settings (Specific) tab.
* The Setting: Look for debounce. Set this to 2.
* The Setting: Look for min_report_interval. Set this to 60.

Why: This tells Z2M: "If you get multiple messages in 2 seconds, only keep the last one. And don't give me a temperature update more than once a minute."

## Firmware Update

https://darkxst.github.io/silabs-firmware-builder/

