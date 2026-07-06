# Lab 6 — Automate with n8n — Triggers, Workflows and AI

**Course:** Internet of Things (IoT) Fundamental for Beginners (TGS-2020504020)
**Topic 04:** IoT Data Analytics and Visualization  (A4, K5, K6)
**Objective:** Data analytics and visualization on cloud — n8n automation & AI insight (LO4)
**Platform tutorial:** https://iot.tertiaryinfotech.com/tutorials/automate-with-n8n

## Goal

The learner connects IoTFlow to n8n with a webhook, picks a trigger (telemetry, alert, online/offline, command), then builds a no-code workflow that notifies, logs to a sheet, calls AI for insight and even controls the device back.

## What you'll build

An n8n workflow fired by device events: threshold alert → notify + log + AI summary

*Uses: IoTFlow Automations, n8n Webhook node, alert rules, Email/Telegram, Google Sheets, AI nodes.*

![Platform walkthrough](../courseware/assets/lab-06-n8n.png)

## Prerequisites

- An account on IoTFlow (https://iot.tertiaryinfotech.com) — created in Lab 1.
- A modern browser. Hardware (ESP32/ESP8266/Raspberry Pi) is optional — every lab can be completed with cURL/Python from any terminal.

- Your device token from Lab 1 (`dev_...`).
- Python 3 with the official client installed: `pip install "iotflow[mqtt]"` ([PyPI](https://pypi.org/project/iotflow/) · [source & examples](https://github.com/alfredang/iotplatform/tree/main/clients/python)).

## Step-by-step

### Step 1 — In n8n, add a Webhook node to a new workflow, activate the workflow, and copy the webhook's Production URL.

### Step 2 — In IoTFlow, create a new Automation and choose the trigger type: telemetry received, alert fired, device online/offline, or command sent.

### Step 3 — Optionally narrow the trigger by device and metric (e.g. only temperature), then paste the n8n webhook URL and save.

### Step 4 — Create an alert rule on a threshold (e.g. temperature > 30) or device-offline, and hand it off to the automation.

```
Alert rule:  temperature > 30  →  fire automation (n8n webhook)
```

### Step 5 — Use Test to send a sample payload to n8n, inspect the JSON the webhook receives, then enable live triggering.

### Step 6 — In n8n, branch the flow: send an Email/Telegram/WhatsApp notification and append the reading to Google Sheets.

### Step 7 — Add an AI node to summarise the readings and recommend an action — AI-powered analytics with zero code.

### Step 8 — Close the loop: add an HTTP Request node that sends a downlink command back to the device (e.g. switch a fan on).

```
POST {host}/api/device/command   { "pin": "V1", "value": 1 }
```

## Test it

Pushing a reading above the threshold fires the n8n flow: the notification arrives, a row is appended to the sheet, the AI summary is generated, and the device reacts to the command sent back.

---
*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved. · www.tertiarycourses.com.sg*
