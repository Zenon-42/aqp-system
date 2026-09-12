# 🌍 Air Quality Prediction & Monitoring System

A machine learning–based web application that monitors air quality for a selected city and predicts its air-quality category using real-time pollutant data.

The application combines **Flask**, **OpenWeatherMap air-pollution data**, and a trained **K-Nearest Neighbors (KNN)** model to provide an easy way to check air-quality conditions.

## 🚀 Features

* 🌆 Search air quality by city
* 🌐 Fetch real-time air-pollution data using OpenWeatherMap
* 🧪 Monitor major pollutants:

  * PM2.5
  * PM10
  * NO₂
  * SO₂
* 📊 Convert pollutant values into corresponding pollutant indices
* 🤖 Predict air-quality category using a trained KNN model
* 📡 REST API endpoint for live AQI prediction
* 📈 Model comparison endpoint
* 🖥️ Flask-based web interface

## 🧠 How It Works

The system follows this basic workflow:

```text
User enters city
       ↓
OpenWeatherMap Geocoding API
       ↓
Latitude & Longitude
       ↓
OpenWeatherMap Air Pollution API
       ↓
Pollutant concentrations
       ↓
SO₂ / NO₂ / PM2.5 / PM10 indices
       ↓
Trained KNN Model
       ↓
Air Quality Prediction
       ↓
Result displayed to the user
```

## 🛠️ Tech Stack

| Technology          | Purpose                                  |
| ------------------- | ---------------------------------------- |
| Python              | Core programming language                |
| Flask               | Web application and API                  |
| NumPy               | Numerical processing                     |
| Scikit-learn        | Machine learning                         |
| Joblib              | Loading the trained ML model             |
| OpenWeatherMap API  | Real-time weather and air-pollution data |
| HTML/CSS/JavaScript | Frontend                                 |
| Jupyter Notebook    | Data analysis and model development      |

## 🤖 Machine Learning Model

The project uses a trained **K-Nearest Neighbors (KNN)** model stored in:

```text
AQI_KNN.pkl
```

The model receives four processed features:

* SOI — Sulfur Dioxide Index
* NOI — Nitrogen Dioxide Index
* RPI — PM2.5-related index
* SPMI — PM10-related index

These features are generated from the pollutant concentrations retrieved from OpenWeatherMap.

## 📊 Model Comparison

The application includes a model-comparison endpoint with the following recorded scores:

| Model               | Score |
| ------------------- | ----: |
| Random Forest       |  0.89 |
| KNN                 |  0.82 |
| Decision Tree       |  0.78 |
| Logistic Regression |  0.74 |

> These values are the comparison values currently defined in the application.

## 📁 Project Structure

```text
aqp-system/
│
├── static/
│   └── ...
│
├── templates/
│   └── ...
│
├── AQI_KNN.pkl
├── airqmonitoring.csv
├── Copy_of_P107_Air_Pollution_Monitoring_using_.ipynb
├── app.py
├── requirements.txt
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Zenon-42/aqp-system.git
cd aqp-system
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the OpenWeatherMap API key

Create a `.env` file in the project root:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

The application reads the API key from the environment rather than directly storing it in the source code.

### 5. Run the application

```bash
python app.py
```

The Flask server will start on:

```text
http://localhost:5000
```

## 🔌 API Endpoints

### Home

```text
GET /
```

Loads the main web application.

### Live Air Quality

```text
GET /live-aqi?city=Visakhapatnam
```

Returns the pollutant values, calculated indices, and machine-learning prediction for the requested city.

Example response structure:

```json
{
  "city": "Visakhapatnam",
  "prediction": "...",
  "raw_values": {
    "pm2_5": 0,
    "pm10": 0,
    "no2": 0,
    "so2": 0
  },
  "indices": {
    "SOi": 25,
    "Noi": 25,
    "Rpi": 25,
    "SPMi": 25
  }
}
```

### Model Comparison

```text
GET /model-comparison
```

Returns the model comparison values used by the application.

## 📚 Dataset & Notebook

The repository contains the dataset used for the project:

```text
airqmonitoring.csv
```

The machine-learning development and experimentation can be found in:

```text
Copy_of_P107_Air_Pollution_Monitoring_using_.ipynb
```

## 🔐 Environment Variables

The following environment variable is required:

```text
OPENWEATHER_API_KEY
```

Do **not** commit your `.env` file or expose your API key publicly.

## 🎯 Project Goals

This project was developed to explore the practical application of:

* Machine learning
* Environmental data analysis
* Real-time API integration
* Flask web development
* REST APIs
* Data preprocessing
* Model prediction

## 🔮 Future Improvements

Possible improvements include:

* 📍 Automatic location detection
* 📊 Historical AQI charts
* 📅 Air-quality forecasting
* 🌤️ Weather information integration
* 🗺️ Interactive air-quality maps
* 🔔 Pollution alerts
* 📱 Improved responsive UI
* 🔬 More advanced machine-learning models
* 📈 Model evaluation using additional metrics

## 📄 License

This project is available for educational and personal use.

---

⭐ If you find this project useful, consider giving the repository a star!

**GitHub:** https://github.com/Zenon-42/aqp-system
