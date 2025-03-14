from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "your api "
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    forecast_data = None
    error_message = None
    unit = "metric"

    if request.method == "POST":
        city = request.form["city"]
        unit = request.form.get("unit", "metric")

        if city:
            params = {"q": city, "appid": API_KEY, "units": unit}
            response = requests.get(BASE_URL, params=params)
            forecast_response = requests.get(FORECAST_URL, params=params)

            if response.status_code == 200 and forecast_response.status_code == 200:
                weather_data = response.json()
                forecast_data = forecast_response.json()
            else:
                error_message = "City not found. Please try again."

    return render_template("index.html", weather=weather_data, forecast=forecast_data, error=error_message, unit=unit)

if __name__ == "__main__":
    app.run(debug=True)

