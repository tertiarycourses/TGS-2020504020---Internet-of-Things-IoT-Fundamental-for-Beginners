"""
SINGLE SOURCE OF TRUTH for the IoT Fundamental for Beginners courseware.

Every artifact — the slide deck (PPT), Lesson Plan (LP), Learner Guide
(LG DOCX + LEARNER-GUIDE.md mirror) and the labs/ folder — is generated from
the data in this module plus data_labs.py, so titles, topic numbering, labs,
learning outcomes and the schedule can never drift apart.

Edit here, then re-run build_slides.py / build_lesson_plan.py /
build_learner_guide.py / build_labs.py.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Internet of Things (IoT) Fundamental for Beginners"
SHORT_TITLE  = "IoT Fundamental for Beginners"
FILE_STEM    = "IoT-Fundamental-for-Beginners"
COURSE_CODE  = "TGS-2020504020"
VERSION      = "v13"
VERSION_DATE = "6 July 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 2

COURSE_URL   = "https://www.tertiarycourses.com.sg/wsq-internet-of-things-iot-fundamental-for-beginners.html"
PLATFORM     = "IoTFlow"
PLATFORM_URL = "https://iot.tertiaryinfotech.com"
TUTORIALS_URL = "https://iot.tertiaryinfotech.com/tutorials"

# ------------------------------------------------------------------ skills framework
TSC_TITLE = "Internet of Things Application"
TSC_CODE  = "PTP-TEM-3002-1.1"
ABILITIES = [
    "A1: Conduct briefings on the uses and functions of IoT technologies adopted by the organisation",
    "A2: Review IoT testing results and identify areas for improvement",
    "A3: Integrate information from multiple data sources",
    "A4: Review data to produce insights of business value",
]
KNOWLEDGE = [
    "K1: Concept of Internet of Things (IoT)",
    "K2: Types and functionalities of IoT devices",
    "K3: Types of circuits and sensors within devices",
    "K4: Types of wireless communication technologies",
    "K5: Data analytics techniques",
    "K6: Concept of cybersecurity",
]

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Understand the uses and functions of IoT technologies",
    "LO2: Post sensor data to cloud for IoT review",
    "LO3: Control devices from cloud data sources",
    "LO4: Data analytics and visualization on cloud to gain business insight",
]

# ------------------------------------------------------------------ topics
TOPICS = [
    dict(num=1, code="01",
         title="Overview of Internet of Things (IoT)",
         subtitle="What is IoT · Devices, Sensors & Actuators · Triggers · Wireless Technologies · Use Cases",
         tags="A1, K1, K4",
         outline=["What is IoT?",
                  "IoT Devices, Sensors and Actuators",
                  "Triggers and Events",
                  "Wireless Communication Technologies for IoT",
                  "IoT Applications and Use Cases"],
         concepts=[
            "IoT is the network of physical devices embedded with sensors, software and connectivity that collect and exchange data over the internet.",
            "A device senses the world with sensors (input) and acts on it with actuators (output) — a trigger turns a reading into an event that starts an action.",
            "Wireless technologies (Wi-Fi, Bluetooth, Zigbee, LoRaWAN, NB-IoT, 5G) connect constrained devices to the cloud.",
            "IoT powers smart homes, agriculture, healthcare, manufacturing, logistics, retail and smart cities.",
         ]),
    dict(num=2, code="02",
         title="Collect and Post Data to Cloud",
         subtitle="Cloud & IoT Platforms · IoTFlow · Device Registration · MQTT & HTTP Telemetry",
         tags="A2, K3",
         outline=["What is Cloud Computing",
                  "IoT Cloud Platforms — our platform IoTFlow",
                  "Register a Device and Get a Token",
                  "Collect Data with Sensors",
                  "Post Data to Cloud using MQTT or REST API"],
         concepts=[
            "The cloud stores and processes IoT data at scale — devices stream telemetry to an IoT platform instead of a single computer.",
            "IoTFlow (iot.tertiaryinfotech.com) is our low-code IoT platform: connect ESP32/Arduino/Pi over MQTT or HTTP, visualise, control and automate.",
            "Every device authenticates with a device token (Authorization: Bearer dev_...) issued once at registration.",
            "Telemetry is a simple JSON document of metric key-value pairs, e.g. {\"temperature\": 22.5, \"humidity\": 60}.",
         ]),
    dict(num=3, code="03",
         title="Read Data and Remote Control from Cloud",
         subtitle="Read via REST API & MQTT · Virtual Pins · Dashboard Control · Alerts & Triggers",
         tags="A3, K2",
         outline=["Read Data using MQTT or REST API",
                  "Remote Control Devices from Cloud",
                  "Virtual Pins — Blynk-style two-way control",
                  "Alerts and Trigger Rules"],
         concepts=[
            "Reading from the cloud integrates data sources: REST GET for state and history, MQTT subscribe for real-time push.",
            "Virtual pins (V1, relay, pump ...) are named keys that dashboard control widgets write to — buttons, switches, sliders and terminals.",
            "Devices receive downlink commands on the MQTT topic devices/<id>/down, or by HTTP-polling GET /api/device/state.",
            "Alert rules fire on metric thresholds or device-offline, and can hand off to an n8n automation.",
         ]),
    dict(num=4, code="04",
         title="IoT Data Analytics and Visualization",
         subtitle="Dashboards & Widgets · n8n Workflow Automation · AI Analytics · IoT Cybersecurity",
         tags="A4, K5, K6",
         outline=["Visualize IoT Data on Cloud Dashboards",
                  "Analyze IoT Data for Business Insight",
                  "Automate with n8n Workflows",
                  "AI for IoT Analytics",
                  "Cyber Security Concern"],
         concepts=[
            "Dashboards turn raw readings into number cards, gauges, line/bar charts, LED indicators and maps that auto-refresh.",
            "n8n is a low-code workflow automation tool: a device event triggers a flow of nodes that notify, log, call AI or control devices back.",
            "AI nodes in a workflow summarise readings, detect anomalies and generate recommendations — analytics with zero code.",
            "IoT security matters because the cyber and physical worlds converge: spoofing, tampering, eavesdropping, DoS and elevation of privilege.",
         ]),
]

# ------------------------------------------------------------------ platform (IoTFlow)
PLATFORM_TAGLINE = ("Connect Arduino, ESP32 & Raspberry Pi over MQTT or HTTP, control them in "
                    "real time from web and mobile, and automate everything with drag-and-drop n8n flows.")
HOW_IT_WORKS = [
    "Connect — flash the wizard snippet to your ESP32 / Arduino / Pi. It streams data over MQTT or HTTP.",
    "Visualise & Control — compose a dashboard of charts, gauges, buttons & sliders, on web and mobile.",
    "Automate with n8n — device events fire n8n flows that notify, control devices back, log data or call AI.",
]
PLATFORM_FEATURES = [
    ("Device Connectivity", "Guided wizard with copy-paste code for ESP32, Arduino, Raspberry Pi, C++ & Python over MQTT or HTTP."),
    ("Two-way Control", "Buttons, switches & sliders write to virtual pins — control relays, motors & LEDs live, Blynk-style."),
    ("Low-code Automation", "Drag-and-drop n8n flows react to device events — notify, control, log, or call AI with zero code."),
    ("Dashboard", "Live telemetry with auto-refresh, number cards, charts, gauges, LED indicators & maps."),
    ("Messaging Protocols", "A managed MQTT broker and a simple REST endpoint. Uplink telemetry and downlink commands."),
    ("Alerts", "Trigger on thresholds or device-offline, then hand off to an n8n flow."),
    ("Cross-platform Apps", "Installable PWA — add IoTFlow to your phone's home screen for mobile control."),
    ("Self-hosted", "Docker & Coolify-ready. Own your data and your automation engine."),
]
INDUSTRIES = ["Smart Agriculture", "Industrial IoT", "Smart Home", "Energy & Utilities",
              "Healthcare & Cold Chain", "Smart Buildings", "Logistics & Fleet",
              "Water Management", "Retail & Vending"]

# ------------------------------------------------------------------ schedule themes
DAY_THEMES = {
    1: "IoT Overview & Collecting Data to the Cloud",
    2: "Remote Control, Analytics, n8n Automation & Assessment",
}

# ------------------------------------------------------------------ assessment
ASSESSMENT = dict(
    written="Written Assessment (WA) — Short-Answer Questions (SAQ), 1 hour, open book.",
    practical="Practical Performance (PP) — hands-on IoT platform tasks, 1 hour, open book.",
    note="A minimum of 75% attendance is required to be eligible for assessment and funding.",
)

RECOMMENDED_COURSES = [
    "WSQ - Creating High-Converting Email Campaigns with Mailchimp",
    "WSQ - Data Mining and Machine Learning Fundamentals for Beginners",
    "WSQ - Business Innovation with Blockchain Technology",
    "WSQ - Predictive Analytics with PyTorch: Transform Your Data to Prediction",
    "WSQ - Search Engine Optimization (SEO) for Small and Medium Enterprises",
]
