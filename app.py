from flask import Flask, request, jsonify, render_template_string
import requests
import os

app = Flask(__name__)

# 🔑 Put your API key here OR use environment variable
API_KEY = os.getenv("API_KEY") or "YOUR_API_KEY_HERE"

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Weather Dashboard</title>
    </head>
    <body style="text-align:center; font-family:Arial;">
        <h2>Weather Dashboard</h2>
        <input type="text" id="city" placeholder="Enter city">
        <button onclick="getWeather()">Get Weather</button>
        <p id="result"></p>

        <script>
            function getWeather() {
                let city = document.getElementById("city").value;

                fetch(`/weather?city=${city}`)
                .then(res => res.json())
                .then(data => {
                    if(data.error){
                        alert(data.error);
                    } else {
                        document.getElementById("result").innerHTML =
                            "Temperature: " + data.temp + "°C<br>" +
                            "Humidity: " + data.humidity + "%<br>" +
                            "Condition: " + data.description;
                    }
                })
                .catch(err => {
                    alert("Server error!");
                });
            }
        </script>
    </body>
    </html>
    ''')

@app.route('/weather')
def weather():
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "Please enter a city name"})

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            return jsonify({"error": "API request failed"})

        data = response.json()

        # 🔥 Handle city not found
        if data.get("cod") != 200:
            return jsonify({"error": data.get("message", "City not found")})

        result = {
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": "Server error"})

if __name__ == "__main__":
    app.run(debug=True)