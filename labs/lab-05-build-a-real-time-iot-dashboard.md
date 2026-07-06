# Lab 5 — Build a Real-Time IoT Dashboard

**Course:** Internet of Things (IoT) Fundamental for Beginners (TGS-2020504020)
**Topic 04:** IoT Data Analytics and Visualization  (A4, K5, K6)
**Objective:** Data analytics and visualization on cloud — dashboards (LO4)
**Platform tutorial:** https://iot.tertiaryinfotech.com/tutorials/build-a-dashboard

## Goal

The learner turns raw readings into a live dashboard — number cards, gauges, line/bar charts, LED indicators, device status and maps — arranged on a responsive grid that auto-refreshes.

## What you'll build

A monitoring dashboard with a number card, gauge, chart, LED indicator and map

*Uses: Display widgets: number card, gauge, line/bar chart, LED, device status, alert list, map.*

![Platform walkthrough](../courseware/assets/lab-05-dashboard.png)

## Prerequisites

- An account on IoTFlow (https://iot.tertiaryinfotech.com) — created in Lab 1.
- A modern browser. Hardware (ESP32/ESP8266/Raspberry Pi) is optional — every lab can be completed with cURL/Python from any terminal.

- Your device token from Lab 1 (`dev_...`).

## Step-by-step

### Step 1 — On the Dashboard click Add widget — widgets are grouped into Display (show data) and Control (send commands).

### Step 2 — Add a Number card: select your device, choose the metric (temperature) and give the widget a title.

### Step 3 — Add a Gauge for humidity and set sensible min/max bounds (e.g. 0–100 %).

### Step 4 — Add a Line chart to plot the temperature history over time.

### Step 5 — Add an LED indicator (on/off state) and a Map widget if your device reports a location.

### Step 6 — Arrange the layout — widgets snap into a responsive grid, refresh automatically, and can be removed with the trash icon.

## Test it

Send fresh readings (Lab 2) and watch every widget — card, gauge and chart — update live within the 5-second auto-refresh.

---
*© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved. · www.tertiarycourses.com.sg*
