"""The 6 hands-on labs — single source shared by the PPT, LP, LG and labs/.

Each lab mirrors an official IoTFlow tutorial on
https://iot.tertiaryinfotech.com/tutorials so learners can revisit the same
steps after class. steps = list of (instruction, code/command) tuples.
"""

HOST = "https://iot.tertiaryinfotech.com"

LABS = [
    # ---------------------------------------------------------------- Topic 2
    dict(
        num=1, shot="lab-01-add-device.png", topic=2,
        title="Register Your First Device on IoTFlow",
        objective="Post sensor data to cloud for IoT review — register a device (LO2)",
        tutorial=f"{HOST}/tutorials/add-your-first-device",
        desc=("The learner signs in to the IoTFlow platform, creates a project workspace, runs the "
              "Add Device wizard, chooses a protocol (HTTP or MQTT) and obtains the device token "
              "used to authenticate every message the device sends."),
        build="A registered IoT device in your own IoTFlow project, with its device token saved",
        services="IoTFlow projects, Add Device wizard, device tokens, MQTT & HTTP protocols",
        steps=[
            ("Open the IoTFlow platform and sign up for a free account (or log in).",
             "https://iot.tertiaryinfotech.com  →  Sign up  →  Log in"),
            ("Pick or create a project — a self-contained workspace with its own dashboard, alerts, map and automations. Use the project switcher at the top of the sidebar.",
             ""),
            ("Click Add Device in the sidebar and give your device a descriptive name.",
             'Device name:  Living Room Sensor'),
            ("Follow the six-step guided wizard and choose a protocol: HTTP — simplest, POST JSON to a REST endpoint; or MQTT — lightweight pub/sub, ideal for many devices and real-time control. Both remain available later.",
             ""),
            ("Copy the device token shown when the device is created — it is displayed only once.",
             "dev_XXXXXXXXXXXX"),
            ("Understand how the token authenticates every message your device sends.",
             "Authorization: Bearer dev_XXXXXXXXXXXX"),
        ],
        test=("The new device appears in your project's device list, and the Integrate page shows "
              "code snippets pre-filled with your endpoint and device token."),
    ),
    dict(
        num=2, shot="lab-02-send-reading.png", topic=2,
        title="Send Sensor Readings to the Cloud (HTTP & MQTT)",
        objective="Post sensor data to cloud for IoT review — send telemetry (LO2)",
        tutorial=f"{HOST}/tutorials/send-your-first-reading",
        desc=("The learner pushes sensor values to the IoTFlow telemetry API three ways — cURL from "
              "any terminal, the Python client, and an ESP32/ESP8266 over MQTT — and watches the "
              "readings appear live on the dashboard."),
        build="Live temperature & humidity telemetry streaming into IoTFlow from terminal, Python and ESP32",
        services="Telemetry REST API, Python client (pip install iotflow), ESP32/ESP8266 Arduino library, MQTT broker (port 1883)",
        steps=[
            ("Open the Integrate page for your device — every snippet comes pre-filled with your endpoint and device token.",
             ""),
            ("Send your first reading from any terminal with cURL (HTTP POST).",
             'curl -X POST https://iot.tertiaryinfotech.com/api/telemetry \\\n  -H "Authorization: Bearer dev_XXXXXXXXXXXX" \\\n  -H "Content-Type: application/json" \\\n  -d \'{"temperature": 22.5, "humidity": 60}\''),
            ("Open the Dashboard — the reading appears under Latest Telemetry within seconds (widgets auto-refresh every 5 s).",
             ""),
            ("Install the official IoTFlow Python client from PyPI (https://pypi.org/project/iotflow/).",
             'pip install "iotflow[mqtt]"      # with real-time MQTT (paho-mqtt)\npip install iotflow               # HTTP only — zero dependencies'),
            ("Send readings from Python over HTTP — several metrics at once with send(), or one at a time with virtual_write().",
             'from iotflow import IoTFlow\n\niot = IoTFlow("https://iot.tertiaryinfotech.com", "dev_XXXXXXXXXXXX", "living-room-sensor")\niot.send(temperature=22.5, humidity=60)      # several metrics at once\niot.virtual_write("temperature", 22.5)       # or one at a time'),
            ("Stream continuously over MQTT with the telemetry_upload.py example — download it, fill in your broker host, device id and device token, then run it.",
             'curl -O https://raw.githubusercontent.com/alfredang/iotplatform/main/clients/python/examples/telemetry_upload.py\n# edit: MQTT_BROKER = "iot.tertiaryinfotech.com", DEVICE_ID, DEVICE_TOKEN\npython telemetry_upload.py'),
            ("Study the loop inside telemetry_upload.py — connect() runs MQTT in the background and mqtt_publish() sends a reading every 10 seconds.",
             'iot = IoTFlow(token=DEVICE_TOKEN, device_id=DEVICE_ID,\n              mqtt_host=MQTT_BROKER, mqtt_port=MQTT_PORT)\niot.connect()                    # MQTT runs in the background\nwhile True:\n    iot.mqtt_publish(temperature=temperature, humidity=humidity, voltage=3.7)\n    time.sleep(PUBLISH_INTERVAL_S)'),
            ("Hardware alternative: flash the ESP8266_Telemetry_Upload Arduino sketch — the Arduino library speaks the same protocol as the Python client. Confirm the values update live on the dashboard.",
             'IoTFlow.virtualWrite("temperature", t);   // metric name binds to dashboard widgets'),
        ],
        test=("Each value you send appears in the Dashboard's Latest Telemetry within seconds, "
              "and the device's telemetry history grows with every reading."),
    ),
    # ---------------------------------------------------------------- Topic 3
    dict(
        num=3, shot="lab-03-tutorials.png", topic=3,
        title="Read Device Data from the Cloud (REST API & MQTT)",
        objective="Control devices from cloud data sources — read data (LO3)",
        tutorial=f"{HOST}/tutorials",
        desc=("The learner reads device data back out of the cloud — the latest state over the REST "
              "API, real-time messages by subscribing to the device's MQTT topics, and per-device "
              "telemetry history on the platform — integrating data from multiple sources."),
        build="A terminal and Python session reading live device state and streaming MQTT messages",
        services="REST API (GET /api/device/state), MQTT subscribe (devices/<id>/down), telemetry history",
        steps=[
            ("Read your device's latest state from any terminal over the REST API.",
             'curl https://iot.tertiaryinfotech.com/api/device/state \\\n  -H "Authorization: Bearer dev_XXXXXXXXXXXX"'),
            ("Inspect the JSON reply — the platform returns the current value of every metric and virtual pin.",
             ""),
            ("Subscribe to your device's MQTT downlink topic to watch commands and data arrive in real time.",
             'mosquitto_sub -h iot.tertiaryinfotech.com -p 1883 \\\n  -u device -P dev_XXXXXXXXXXXX -t "devices/<id>/down" -v'),
            ("Send a fresh reading (Lab 2) and watch it flow through — uplink telemetry vs downlink commands.",
             ""),
            ("Open the device page on IoTFlow and review its per-device telemetry history and active alerts.",
             ""),
            ("Read the same state from Python and print the values — this is how any external app integrates IoT data.",
             'r = requests.get(f"{host}/api/device/state",\n    headers={"Authorization": f"Bearer {token}"})\nprint(r.json())'),
        ],
        test=("The REST call returns the same values shown on the dashboard, and the MQTT "
              "subscription prints messages the moment they are published."),
    ),
    dict(
        num=4, shot="lab-04-control-device.png", topic=3,
        title="Remote Control a Device with Dashboard Virtual Pins",
        objective="Control devices from cloud data sources — remote control (LO3)",
        tutorial=f"{HOST}/tutorials/control-a-device",
        desc=("The learner adds Control widgets (button, switch, slider, terminal) bound to virtual "
              "pins, implements the device-side command handler, and flips a relay/LED live from the "
              "dashboard — Blynk-style two-way control."),
        build="A dashboard switch and slider that control a relay/LED on the device in real time",
        services="Control widgets (Button, Switch, Slider, Terminal), virtual pins, Python client @on_command, MQTT downlink, HTTP polling",
        steps=[
            ("On the Dashboard click Add widget and choose a Control type: Button (momentary), Switch (toggle), Slider (value) or Terminal (text).",
             ""),
            ("Assign the virtual pin the widget writes to — e.g. V1, relay or pump. For a slider also set the min/max range.",
             'Virtual pin:  V1'),
            ("Understand the downlink path — devices receive commands via MQTT on their command topic, or by HTTP polling.",
             'MQTT topic:  devices/<id>/down      HTTP:  GET /api/device/state'),
            ("React to commands in Python with the iotflow client — decorate a handler with @iot.on_command and poll over HTTP (no extra dependencies).",
             'from iotflow import IoTFlow\n\niot = IoTFlow("https://iot.tertiaryinfotech.com", "dev_XXXXXXXXXXXX", "living-room-sensor")\n\n@iot.on_command\ndef handle(pin, value, text):\n    if pin == "V1":\n        print("relay ->", value)      # drive a GPIO here\n\niot.run(interval=3)                   # blocks, polls every 3 s'),
            ("For real-time control, use the same handler over MQTT — loop_forever() keeps the connection open so commands arrive instantly.",
             'iot = IoTFlow(token="dev_XXXXXXXXXXXX", device_id="living-room-sensor",\n              mqtt_host="iot.tertiaryinfotech.com", mqtt_port=1883)\n\n@iot.on_command\ndef handle(pin, value, text): ...\n\niot.loop_forever()'),
            ("Hardware alternative: implement the same handler in the Arduino sketch and map pins to GPIO outputs.",
             'void onCommand(const String& pin, float value, const String& text) {\n  if (pin == "V1") digitalWrite(RELAY_PIN, value > 0 ? HIGH : LOW);\n}'),
            ("Flip the switch and move the slider on the dashboard — commands are delivered to the device immediately; the relay/LED responds. The same events can also trigger automations (Lab 6).",
             ""),
        ],
        test=("Toggling the dashboard switch changes the relay/LED state within a second, and the "
              "slider value arrives in your @on_command handler as you drag it."),
    ),
    # ---------------------------------------------------------------- Topic 4
    dict(
        num=5, shot="lab-05-dashboard.png", topic=4,
        title="Build a Real-Time IoT Dashboard",
        objective="Data analytics and visualization on cloud — dashboards (LO4)",
        tutorial=f"{HOST}/tutorials/build-a-dashboard",
        desc=("The learner turns raw readings into a live dashboard — number cards, gauges, "
              "line/bar charts, LED indicators, device status and maps — arranged on a responsive "
              "grid that auto-refreshes."),
        build="A monitoring dashboard with a number card, gauge, chart, LED indicator and map",
        services="Display widgets: number card, gauge, line/bar chart, LED, device status, alert list, map",
        steps=[
            ("On the Dashboard click Add widget — widgets are grouped into Display (show data) and Control (send commands).",
             ""),
            ("Add a Number card: select your device, choose the metric (temperature) and give the widget a title.",
             ""),
            ("Add a Gauge for humidity and set sensible min/max bounds (e.g. 0–100 %).",
             ""),
            ("Add a Line chart to plot the temperature history over time.",
             ""),
            ("Add an LED indicator (on/off state) and a Map widget if your device reports a location.",
             ""),
            ("Arrange the layout — widgets snap into a responsive grid, refresh automatically, and can be removed with the trash icon.",
             ""),
        ],
        test=("Send fresh readings (Lab 2) and watch every widget — card, gauge and chart — "
              "update live within the 5-second auto-refresh."),
    ),
    dict(
        num=6, shot="lab-06-n8n.png", topic=4,
        title="Automate with n8n — Triggers, Workflows and AI",
        objective="Data analytics and visualization on cloud — n8n automation & AI insight (LO4)",
        tutorial=f"{HOST}/tutorials/automate-with-n8n",
        desc=("The learner connects IoTFlow to n8n with a webhook, picks a trigger (telemetry, "
              "alert, online/offline, command), then builds a no-code workflow that notifies, logs "
              "to a sheet, calls AI for insight and even controls the device back."),
        build="An n8n workflow fired by device events: threshold alert → notify + log + AI summary",
        services="IoTFlow Automations, n8n Webhook node, alert rules, Email/Telegram, Google Sheets, AI nodes",
        steps=[
            ("In n8n, add a Webhook node to a new workflow, activate the workflow, and copy the webhook's Production URL.",
             ""),
            ("In IoTFlow, create a new Automation and choose the trigger type: telemetry received, alert fired, device online/offline, or command sent.",
             ""),
            ("Optionally narrow the trigger by device and metric (e.g. only temperature), then paste the n8n webhook URL and save.",
             ""),
            ("Create an alert rule on a threshold (e.g. temperature > 30) or device-offline, and hand it off to the automation.",
             'Alert rule:  temperature > 30  →  fire automation (n8n webhook)'),
            ("Use Test to send a sample payload to n8n, inspect the JSON the webhook receives, then enable live triggering.",
             ""),
            ("In n8n, branch the flow: send an Email/Telegram/WhatsApp notification and append the reading to Google Sheets.",
             ""),
            ("Add an AI node to summarise the readings and recommend an action — AI-powered analytics with zero code.",
             ""),
            ("Close the loop: add an HTTP Request node that sends a downlink command back to the device (e.g. switch a fan on).",
             'POST {host}/api/device/command   { "pin": "V1", "value": 1 }'),
        ],
        test=("Pushing a reading above the threshold fires the n8n flow: the notification arrives, "
              "a row is appended to the sheet, the AI summary is generated, and the device reacts "
              "to the command sent back."),
    ),
]
