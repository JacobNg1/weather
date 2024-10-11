from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# 配置你的API密钥
API_KEY = 'your_openweathermap_api_key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# 全局错误处理
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city_name = request.form.get('city')
    if not city_name:
        return jsonify({"error": "City name is required"}), 400

    try:
        params = {
            'q': city_name,
            'appid': API_KEY,
            'units': 'metric',
            'lang': 'zh_cn'
        }
        response = requests.get(BASE_URL, params=params)
        if response.status_code != 200:
            return jsonify({"error": f"Error fetching data: {response.status_code}"}), response.status_code

        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return jsonify(weather)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
