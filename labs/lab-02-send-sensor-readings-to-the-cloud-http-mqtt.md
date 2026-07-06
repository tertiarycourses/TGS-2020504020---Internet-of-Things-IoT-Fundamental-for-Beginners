# Lab 2 — Send Sensor Readings to the Cloud (HTTP & MQTT)

**Course:** Internet of Things (IoT) Fundamental for Beginners (TGS-2020504020)
**Topic 02:** Collect and Post Data to Cloud  (A2, K3)
**Objective:** Post sensor data to cloud for IoT review — send telemetry (LO2)
**Platform tutorial:** https://iot.tertiaryinfotech.com/tutorials/send-your-first-reading

## Goal

The learner pushes sensor values to the IoTFlow telemetry API three ways — cURL from any terminal, the Python client, and an ESP32/ESP8266 over MQTT — and watches the readings appear live on the dashboard.

## What you'll build

Live temperature & humidity telemetry streaming into IoTFlow from terminal, Python and ESP32

*Uses: Telemetry REST API, Python iotflow client, ESP32/ESP8266 Arduino library, MQTT broker (port 1883).*

![Platform walkthrough](../courseware/assets/lab-02-send-reading.png)

## Prerequisites

- An account on IoTFlow (https://iot.tertiaryinfotech.com) — created in Lab 1.
- A modern browser. Hardware (ESP32/ESP8266/Raspberry Pi) is optional — every lab can be completed with cURL/Python from any terminal.

- Your device token from Lab 1 (`dev_...`).

## Step-by-step

### Step 1 — Open the Integrate page for your device — every snippet comes pre-filled with your endpoint and device token.

### Step 2 — Send your first reading from any terminal with cURL (HTTP POST).

```
curl -X POST https://iot.tertiaryinfotech.com/api/telemetry \
  -H "Authorization: Bearer dev_XXXXXXXXXXXX" \
  -H "Content-Type: application/json" \
  -d '{"temperature": 22.5, "humidity": 60}'
```

### Step 3 — Open the Dashboard — the reading appears under Latest Telemetry within seconds (widgets auto-refresh every 5 s).

### Step 4 — Send readings from Python using the lightweight iotflow.py client (plain HTTP — no pip install needed).

```
client = IoTFlow(host, device_token, device_id)
client.send(temperature=23.1, humidity=58)
```

### Step 5 — For real hardware: flash the ESP32/ESP8266 Arduino sketch — set your Wi-Fi SSID/password, the broker host (port 1883) and your device credentials.

```
IoTFlow.virtualWrite("temperature", t);   // metric name binds to dashboard widgets
```

### Step 6 — Let the device publish continuously and confirm the values update live on the dashboard.

## Test it

Each value you send appears in the Dashboard's Latest Telemetry within seconds, and the device's telemetry history grows with every reading.

---
*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved. · www.tertiarycourses.com.sg*
