# Lab 4 — Remote Control a Device with Dashboard Virtual Pins

**Course:** Internet of Things (IoT) Fundamental for Beginners (TGS-2020504020)
**Topic 03:** Read Data and Remote Control from Cloud  (A3, K2)
**Objective:** Control devices from cloud data sources — remote control (LO3)
**Platform tutorial:** https://iot.tertiaryinfotech.com/tutorials/control-a-device

## Goal

The learner adds Control widgets (button, switch, slider, terminal) bound to virtual pins, implements the device-side command handler, and flips a relay/LED live from the dashboard — Blynk-style two-way control.

## What you'll build

A dashboard switch and slider that control a relay/LED on the device in real time

*Uses: Control widgets (Button, Switch, Slider, Terminal), virtual pins, MQTT downlink, HTTP polling.*

![Platform walkthrough](../courseware/assets/lab-04-control-device.png)

## Prerequisites

- An account on IoTFlow (https://iot.tertiaryinfotech.com) — created in Lab 1.
- A modern browser. Hardware (ESP32/ESP8266/Raspberry Pi) is optional — every lab can be completed with cURL/Python from any terminal.

- Your device token from Lab 1 (`dev_...`).

## Step-by-step

### Step 1 — On the Dashboard click Add widget and choose a Control type: Button (momentary), Switch (toggle), Slider (value) or Terminal (text).

### Step 2 — Assign the virtual pin the widget writes to — e.g. V1, relay or pump. For a slider also set the min/max range.

```
Virtual pin:  V1
```

### Step 3 — Understand the downlink path — devices receive commands via MQTT on their command topic, or by HTTP polling.

```
MQTT topic:  devices/<id>/down      HTTP:  GET /api/device/state
```

### Step 4 — Implement the command handler in your device sketch and map pins to GPIO outputs.

```
void onCommand(const String& pin, float value, const String& text) {
  if (pin == "V1") digitalWrite(RELAY_PIN, value > 0 ? HIGH : LOW);
}
```

### Step 5 — Flip the switch and move the slider on the dashboard — commands are delivered to the device immediately.

### Step 6 — Observe the relay/LED respond, and note that the same events can also trigger automations (Lab 6).

## Test it

Toggling the dashboard switch changes the relay/LED state within a second, and the slider value arrives in the onCommand handler as you drag it.

---
*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved. · www.tertiarycourses.com.sg*
