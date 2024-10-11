from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# City codes for different cities
CITY_CODES = {
    "Beijing": "101010100",
    "Shanghai": "101020100",
    "Guangzhou": "101280101",
    "Shenzhen": "101280601",
    "Chengdu": "101270101",
    # 可以添加更多城市及其城市代码
}


@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = {}

    if request.method == 'POST':
        city_name = request.form['city']
        city_code = CITY_CODES.get(city_name)

        if city_code:
            response = requests.get(f"http://t.weather.itboy.net/api/weather/city/{city_code}")
            weather_data = response.json()

    return render_template('index.html', weather=weather_data, cities=CITY_CODES.keys())


if __name__ == '__main__':
    app.run(debug=True)
