# Setup Guide — Smart Irrigation Advisor IoT System

This guide explains how to set up the complete system from scratch.

---

## Part 1 — Firebase Setup

**Step 1:** Go to https://console.firebase.google.com and create a new project (e.g., `SmartFarm`).

**Step 2:** Navigate to Build → Realtime Database → Create Database → Start in Test Mode.

**Step 3:** Open the Rules tab and set:
```json
{
  "rules": {
    ".read": true,
    ".write": true
  }
}
```
Click **Publish**.

**Step 4:** Go to the Data tab and create this structure manually:
```
smartfarm
  soil_moisture : 40
  temperature   : 30
  weather       : Sunny
  crop          : Tomato
```

**Step 5:** Copy your database URL (e.g., `https://smartfarm-default-rtdb.firebaseio.com/`). You will need this for both the Raspberry Pi code and the MIT App Inventor app.

---

## Part 2 — OpenWeather API Setup

**Step 1:** Create a free account at https://openweathermap.org

**Step 2:** Go to API Keys and copy your key.

**Step 3:** Test the API in your browser:
```
https://api.openweathermap.org/data/2.5/weather?q=Coimbatore&appid=YOUR_API_KEY&units=metric
```

---

## Part 3 — MIT App Inventor (Mobile App)

**Step 1:** Go to https://appinventor.mit.edu and click **Create Apps**.

**Step 2:** Create a new project named `SmartFarmApp`.

**Step 3:** In Designer view, add these components:
- Labels (for Crop, Soil Moisture, Temperature, Weather, Recommendation)
- Buttons (for crop selection and navigation)
- FirebaseDB (from Storage palette)
- Web component (for OpenWeather API)
- Clock (set TimerInterval to 10000)
- Notifier (for alerts)
- Chart extension (for moisture history graph)

**Step 4:** Configure FirebaseDB:
- Set `FirebaseURL` property to your database URL from Part 1.

**Step 5:** In Blocks editor, add logic to:
- Retrieve Firebase data on screen initialize and every 10 seconds
- Fetch weather data from OpenWeather API
- Compare soil moisture to crop threshold and display recommendation
- Trigger notifier alert when moisture is below minimum

**Step 6:** Build the APK — go to Build → Android App (.apk) and install on your phone.

---

## Part 4 — Raspberry Pi Hardware Setup

> ⚠️ Complete Parts 1–3 first. Test the app with manual Firebase data before connecting hardware.

**Step 1:** Install Raspberry Pi OS on your Raspberry Pi 4.

**Step 2:** Connect the MCP3008 ADC to the Raspberry Pi GPIO pins via breadboard.

**Step 3:** Connect the capacitive soil moisture sensor to Channel 0 of the MCP3008.

**Step 4:** Enable SPI on the Raspberry Pi:
```bash
sudo raspi-config
→ Interface Options → SPI → Enable
```

**Step 5:** Install required Python libraries:
```bash
pip install spidev requests
```

**Step 6:** Open `raspberry_pi/soil_sensor.py` and replace the Firebase URL with your own:
```python
firebase_url = "https://your-project-id.firebaseio.com/soil_moisture.json"
```

**Step 7:** Run the script:
```bash
python3 soil_sensor.py
```

The Raspberry Pi will now read soil moisture every 10 seconds and push the value to Firebase. Your mobile app will update automatically.

---

## Verification Checklist

| Step | Check |
|---|---|
| Firebase database created and rules set | ✅ |
| Firebase URL copied correctly | ✅ |
| OpenWeather API key obtained | ✅ |
| MIT App Inventor app built and installed | ✅ |
| App retrieving data from Firebase | ✅ |
| App displaying weather correctly | ✅ |
| Recommendation logic working | ✅ |
| Alert notification triggering | ✅ |
| Raspberry Pi SPI enabled | ⬜ |
| Python script running and pushing data | ⬜ |
