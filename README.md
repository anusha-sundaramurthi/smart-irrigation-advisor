# Smart Irrigation IoT System 🌱

An IoT-based agriculture monitoring system that measures soil moisture in real time and provides irrigation recommendations to farmers through a mobile application.

---

## Technologies Used

| Layer | Technology |
|---|---|
| Hardware | Raspberry Pi 4, Capacitive Soil Moisture Sensor, MCP3008 ADC |
| Cloud Database | Firebase Realtime Database |
| Mobile App | MIT App Inventor |
| Weather Data | OpenWeather API |
| Programming | Python (Raspberry Pi) |

---

## System Architecture

```
Soil Moisture Sensor
       ↓
  Raspberry Pi 4 (Python)
       ↓
Firebase Realtime Database
       ↓
  MIT App Inventor App
       ↓
OpenWeather API Integration
       ↓
  Irrigation Recommendation → Farmer
```

---

## Features

- 📊 Real-time soil moisture monitoring
- 🌤️ Live weather data integration
- 💧 Smart irrigation recommendation logic
- 📱 Simple mobile dashboard for farmers
- 📈 Moisture history graph (daily & weekly)
- 🔔 Push alert when soil moisture is critically low
- 🌾 Multi-crop support (Tomato, Chilli, Rice, Groundnut, Sugarcane)

---

## Hardware Components

- Raspberry Pi 4
- Capacitive Soil Moisture Sensor
- MCP3008 ADC (analog-to-digital converter)
- Breadboard and jumper wires
- WiFi connection

---

## Repository Structure

```
smart-irrigation-iot/
│
├── README.md
├── report/
│   └── smart_irrigation_advisor - report.pdf
│
├── raspberry_pi/
│   └── soil_sensor.py
│
├── mobile_app/
│   └── mit_app_inventor_notes.md
│
├── diagrams/
│   ├── system_architecture.png
│   ├── circuit_diagram.png
│   └── data_flow.png
│
└── docs/
    └── setup_guide.md
```

---

## Mobile App Screens

| Screen | Description |
|---|---|
| Crop Selection | Farmer selects crop type |
| Dashboard | Live soil moisture, temperature, weather, recommendation |
| Moisture History | Line graph of moisture readings over time |

### Screen 1 — Crop Selection
![Crop Selection Screen](images/screen1.png)

### Screen 2 — Dashboard
![Dashboard Screen](images/screen2.png)

### Screen 3 — Moisture History
![Moisture History Screen](images/screen3.png)

---

## Irrigation Decision Logic

```
If soil_moisture < crop_minimum AND rain_chance < 40%
→ Water the plant

If soil_moisture < crop_minimum AND rain_chance > 60%
→ Wait for rain

If soil_moisture is within range
→ Moisture is sufficient
```

---

## Project Status

| Component | Status |
|---|---|
| Firebase Database | ✅ Complete |
| OpenWeather API | ✅ Complete |
| MIT App Inventor Mobile App | ✅ Complete & Tested |
| Raspberry Pi Hardware | 🔧 Pending |

> **Note:** The mobile application is fully functional and tested. Firebase and OpenWeather API are live and integrated. The Raspberry Pi hardware integration is the remaining component.

---

## Acknowledgements

- [MIT App Inventor](https://appinventor.mit.edu)
- [Firebase](https://firebase.google.com)
- [OpenWeather API](https://openweathermap.org)
