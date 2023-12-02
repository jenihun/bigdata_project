from flask import Flask, render_template, jsonify, send_from_directory
from wikipedia_data import get_nation_img_url, get_nation_info
import json
from urllib.parse import unquote
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# JSON 파일을 읽어오는 엔드포인트 추가
@app.route('/get_countries_data')
def get_countries_data():
    with open('./data/all_countries_data.json', 'r', encoding='utf-8') as json_file:
        countries_data = json.load(json_file)
    return jsonify(countries_data)

# CSV 파일에서 데이터프레임 읽기
df = pd.read_csv('./data/country.csv')

# 두 개의 열 선택
selected_columns = ['나라', 'ImageURL']

# 선택한 열을 사용하여 각 행을 딕셔너리로 만들어 리스트에 추가
data_list = []
for index, row in df[selected_columns].iterrows():
    data_dict = {'나라': row['나라'], 'ImageURL': row['ImageURL']}
    data_list.append(data_dict)

# 나라 데이터를 가져오는 엔드포인트
@app.route('/get_country_data/<path:encoded_country_name>')
def get_country_data(encoded_country_name):
    # URL 디코딩
    country_name = unquote(encoded_country_name)
    
    info = get_nation_info(country_name)
    for item in data_list:
        if country_name == item['나라']:
            image_url = item['ImageURL']
    
    country_data = {
        'image_url': image_url,
        'info': info
    }
    
    return jsonify(country_data)
    
if __name__ == '__main__':
    app.run(debug=True)