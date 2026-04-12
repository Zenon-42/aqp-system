from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import requests
import joblib
import numpy as np
import os
load_dotenv()

app = Flask(__name__)

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Load model (JOBLIB – notebook compatible)
model = joblib.load("AQI_KNN.pkl")
print("Model loaded:", type(model))

# ---------- AQI INDEX FUNCTIONS ----------
def calculate_soi(so2):
    if so2 <= 40: return 25
    elif so2 <= 80: return 50
    elif so2 <= 380: return 100
    else: return 200

def calculate_noi(no2):
    if no2 <= 40: return 25
    elif no2 <= 80: return 50
    elif no2 <= 180: return 100
    else: return 200

def calculate_rpi(pm25):
    if pm25 <= 30: return 25
    elif pm25 <= 60: return 50
    elif pm25 <= 90: return 100
    else: return 200

def calculate_spmi(pm10):
    if pm10 <= 50: return 25
    elif pm10 <= 100: return 50
    elif pm10 <= 250: return 100
    else: return 200

# ---------- ROUTES ----------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/live-aqi")
def live_aqi():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City not provided"}), 400

    geo_url = (
        "http://api.openweathermap.org/geo/1.0/direct"
        f"?q={city}&limit=1&appid={OPENWEATHER_API_KEY}"
    )
    geo_res = requests.get(geo_url).json()
    if not geo_res:
        return jsonify({"error": "City not found"}), 404

    lat, lon = geo_res[0]["lat"], geo_res[0]["lon"]

    pollution_url = (
        "http://api.openweathermap.org/data/2.5/air_pollution"
        f"?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}"
    )
    pollution_res = requests.get(pollution_url).json()
    comp = pollution_res["list"][0]["components"]

    pm25 = comp.get("pm2_5", 0)
    pm10 = comp.get("pm10", 0)
    no2  = comp.get("no2", 0)
    so2  = comp.get("so2", 0)

    SOi  = calculate_soi(so2)
    Noi  = calculate_noi(no2)
    Rpi  = calculate_rpi(pm25)
    SPMi = calculate_spmi(pm10)

    features = np.array([[SOi, Noi, Rpi, SPMi]])
    prediction = model.predict(features)[0]

    return jsonify({
        "city": city,
        "prediction": prediction,
        "raw_values": {
            "pm2_5": pm25,
            "pm10": pm10,
            "no2": no2,
            "so2": so2
        },
        "indices": {
            "SOi": SOi,
            "Noi": Noi,
            "Rpi": Rpi,
            "SPMi": SPMi
        }
    })

@app.route("/model-comparison")
def model_comparison():
    return jsonify({
        "KNN": 0.82,
        "Random Forest": 0.89,
        "Decision Tree": 0.78,
        "Logistic Regression": 0.74
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
