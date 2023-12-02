from flask import Flask, render_template, jsonify, send_from_directory
from wikipedia_data import get_nation_img_url, get_nation_info
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# JSON 파일을 읽어오는 엔드포인트 추가
@app.route('/get_countries_data')
def get_countries_data():
    with open('all_countries_data.json', 'r', encoding='utf-8') as json_file:
        countries_data = json.load(json_file)
    return jsonify(countries_data)
    
if __name__ == '__main__':
    app.run(debug=True)