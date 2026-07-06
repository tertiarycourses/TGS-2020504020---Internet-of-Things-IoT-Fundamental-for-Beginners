# Lab 2 — Send Sensor Readings to the Cloud (HTTP & MQTT)

**Course:** Internet of Things (IoT) Fundamental for Beginners (TGS-2020504020)
**Topic 02:** Collect and Post Data to Cloud  (A2, K3)
**Objective:** Post sensor data to cloud for IoT review — send telemetry (LO2)
**Platform tutorial:** https://iot.tertiaryinfotech.com/tutorials/send-your-first-reading

## Goal

The learner pushes sensor values to the IoTFlow telemetry API three ways — cURL from any terminal, the Python client, and an ESP32/ESP8266 over MQTT — and watches the readings appear live on the dashboard.

## What you'll build

Live temperature & humidity telemetry streaming into IoTFlow from terminal, Python and ESP32

*Uses: Telemetry REST API, Python client (pip install iotflow), ESP32/ESP8266 Arduino library, MQTT broker (port 1883).*

![Platform walkthrough](../courseware/assets/lab-02-send-reading.png)

## Prerequisites

- An account on IoTFlow (https://iot.tertiaryinfotech.com) — created in Lab 1.
- A modern browser. Hardware (ESP32/ESP8266/Raspberry Pi) is optional — every lab can be completed with cURL/Python from any terminal.

- Your device token from Lab 1 (`dev_...`).
- Python 3 with the official client installed: `pip install "iotflow[mqtt]"` ([PyPI](https://pypi.org/project/iotflow/) · [source & examples](https://github.com/alfredang/iotplatform/tree/main/clients/python)).

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

### Step 4 — Install the official IoTFlow Python client from PyPI (https://pypi.org/project/iotflow/).

```
pip install "iotflow[mqtt]"      # with real-time MQTT (paho-mqtt)
pip install iotflow               # HTTP only — zero dependencies
```

### Step 5 — Send readings from Python over HTTP — several metrics at once with send(), or one at a time with virtual_write().

```
from iotflow import IoTFlow

iot = IoTFlow("https://iot.tertiaryinfotech.com", "dev_XXXXXXXXXXXX", "living-room-sensor")
iot.send(temperature=22.5, humidity=60)      # several metrics at once
iot.virtual_write("temperature", 22.5)       # or one at a time
```

### Step 6 — Stream continuously over MQTT with the telemetry_upload.py example — download it, fill in your broker host, device id and device token, then run it.

```
curl -O https://raw.githubusercontent.com/alfredang/iotplatform/main/clients/python/examples/telemetry_upload.py
# edit: MQTT_BROKER = "iot.tertiaryinfotech.com", DEVICE_ID, DEVICE_TOKEN
python telemetry_upload.py
```

### Step 7 — Study the loop inside telemetry_upload.py — connect() runs MQTT in the background and mqtt_publish() sends a reading every 10 seconds.

```
iot = IoTFlow(token=DEVICE_TOKEN, device_id=DEVICE_ID,
              mqtt_host=MQTT_BROKER, mqtt_port=MQTT_PORT)
iot.connect()                    # MQTT runs in the background
while True:
    iot.mqtt_publish(temperature=temperature, humidity=humidity, voltage=3.7)
    time.sleep(PUBLISH_INTERVAL_S)
```

### Step 8 — Hardware alternative: flash the ESP8266_Telemetry_Upload Arduino sketch — the Arduino library speaks the same protocol as the Python client. Confirm the values update live on the dashboard.

```
IoTFlow.virtualWrite("temperature", t);   // metric name binds to dashboard widgets
```

## Test it

Each value you send appears in the Dashboard's Latest Telemetry within seconds, and the device's telemetry history grows with every reading.

---
*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved. · www.tertiarycourses.com.sg*
