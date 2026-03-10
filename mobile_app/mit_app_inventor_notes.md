# MIT App Inventor — Mobile App Design Notes

## Platform

The mobile application for this project was built using **MIT App Inventor** (https://appinventor.mit.edu), a block-based visual programming environment for Android app development.

MIT App Inventor was chosen because it supports rapid development, integrates natively with Firebase, and requires no complex coding knowledge — making it appropriate for academic IoT projects.

---

## App Screens

### Screen 1 — Crop Selection

**Purpose:** Allow the farmer to select the crop currently being grown.

**Components used:**
- Label: "Smart Irrigation Advisor" (title)
- Label: "Select Your Crop"
- Buttons: Sugar Cane, Rice, Tomato, Chilli, Groundnut

**Logic:**
- When a crop button is clicked, the crop name is stored in Firebase under the key `crop`
- App navigates to Screen 2 (Dashboard)

---

### Screen 2 — Dashboard

**Purpose:** Display real-time sensor data and irrigation recommendation.

**Components used:**
- Labels: Crop, Soil Moisture, Temperature, Weather, Recommendation
- FirebaseDB component — retrieves sensor data
- Web component — calls OpenWeather API
- Clock component — auto-refreshes data every 10 seconds
- Notifier component — shows alert if moisture is low
- Button: "Change Crop" (navigates back to Screen 1)

**Example display:**
```
Crop          : Tomato
Soil Moisture : 38%
Temperature   : 30°C
Weather       : Cloudy

Recommendation: Water Today
```

**Alert trigger:**
```
If soil_moisture < crop_minimum
→ Show notifier: "Soil moisture is low. Please water today."
```

---

### Screen 3 — Moisture History

**Purpose:** Show soil moisture trend over time using a graph.

**Components used:**
- Chart extension — line graph
- FirebaseDB — reads historical moisture values
- Button: "Back to Dashboard"

**Graph displays:**
- X-axis: Time (08:00 to 16:00+)
- Y-axis: Moisture percentage (0–100%)
- Daily and weekly trend view

---

## Firebase Integration

| Property | Value |
|---|---|
| Component | FirebaseDB |
| FirebaseURL | https://your-project-id.firebaseio.com/ |
| Data retrieved | soil_moisture, temperature, weather, crop |

**Block logic:**
```
when Screen.Initialize
  call FirebaseDB.GetValue(tag: "soil_moisture")

when FirebaseDB.GotValue
  set SoilMoistureLabel.Text to value

when Clock.Timer (every 10 seconds)
  call FirebaseDB.GetValue
```

---

## OpenWeather API Integration

**Request URL format:**
```
https://api.openweathermap.org/data/2.5/weather?q=CITY&appid=API_KEY&units=metric
```

**Block logic:**
```
when Screen.Initialize
  set Web.Url to weather API URL
  call Web.Get

when Web.GotText
  decode JSON response
  extract temperature and weather description
  update labels
```

---

## Irrigation Recommendation Logic (Blocks)

```
If soil_moisture < crop_minimum
  AND rain_probability < 40
  → set RecommendationLabel to "Water Today"

Else If soil_moisture < crop_minimum
  AND rain_probability > 60
  → set RecommendationLabel to "Wait for Rain"

Else
  → set RecommendationLabel to "Moisture is Sufficient"
```

---

## Crop Moisture Thresholds

| Crop | Minimum (%) | Maximum (%) |
|---|---|---|
| Tomato | 40 | 60 |
| Chilli | 35 | 55 |
| Rice | 70 | 90 |
| Groundnut | 30 | 50 |
| Sugar Cane | 50 | 70 |

---

## App Status

- ✅ All three screens built and functional
- ✅ Firebase connection live and retrieving data
- ✅ OpenWeather API integrated and displaying live weather
- ✅ Recommendation logic working correctly
- ✅ Alert notification triggering when moisture is low
- ✅ Moisture history graph rendering sensor data
