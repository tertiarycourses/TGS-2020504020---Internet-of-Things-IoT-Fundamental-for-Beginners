# Lab 1 — Register Your First Device on IoTFlow

**Course:** Internet of Things (IoT) Fundamental for Beginners (TGS-2020504020)
**Topic 02:** Collect and Post Data to Cloud  (A2, K3)
**Objective:** Post sensor data to cloud for IoT review — register a device (LO2)
**Platform tutorial:** https://iot.tertiaryinfotech.com/tutorials/add-your-first-device

## Goal

The learner signs in to the IoTFlow platform, creates a project workspace, runs the Add Device wizard, chooses a protocol (HTTP or MQTT) and obtains the device token used to authenticate every message the device sends.

## What you'll build

A registered IoT device in your own IoTFlow project, with its device token saved

*Uses: IoTFlow projects, Add Device wizard, device tokens, MQTT & HTTP protocols.*

![Platform walkthrough](../courseware/assets/lab-01-add-device.png)

## Prerequisites

- An account on IoTFlow (https://iot.tertiaryinfotech.com).
- A modern browser. Hardware (ESP32/ESP8266/Raspberry Pi) is optional — every lab can be completed with cURL/Python from any terminal.

## Step-by-step

### Step 1 — Open the IoTFlow platform and sign up for a free account (or log in).

```
https://iot.tertiaryinfotech.com  →  Sign up  →  Log in
```

### Step 2 — Pick or create a project — a self-contained workspace with its own dashboard, alerts, map and automations. Use the project switcher at the top of the sidebar.

### Step 3 — Click Add Device in the sidebar and give your device a descriptive name.

```
Device name:  Living Room Sensor
```

### Step 4 — Follow the six-step guided wizard and choose a protocol: HTTP — simplest, POST JSON to a REST endpoint; or MQTT — lightweight pub/sub, ideal for many devices and real-time control. Both remain available later.

### Step 5 — Copy the device token shown when the device is created — it is displayed only once.

```
dev_XXXXXXXXXXXX
```

### Step 6 — Understand how the token authenticates every message your device sends.

```
Authorization: Bearer dev_XXXXXXXXXXXX
```

## Test it

The new device appears in your project's device list, and the Integrate page shows code snippets pre-filled with your endpoint and device token.

---
*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved. · www.tertiarycourses.com.sg*
