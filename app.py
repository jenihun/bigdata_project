from flask import Flask, render_template, jsonify
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
from geocoding import get_lat_lon_from_country

from wikipedia_data import get_nation_img_url, get_nation_info

countries = [
    'United Kingdom', 'France', 'Germany', 'Italy', 'Spain',
    'Ireland', 'Portugal', 'Belgium', 'Netherlands', 'Denmark',
    'Norway', 'Sweden', 'Finland', 'Poland', 'Czech Republic',
    'Austria', 'Croatia', 'Slovakia', 'Hungary', 'Serbia',
    'Greece', 'Lithuania', 'Estonia', 'Latvia', 'Belarus',
    'Ukraine', 'Romania', 'Bulgaria', 'Moldova', 'Korea',
    'Saudi Arabia', 'Japan', 'Philippines', 'Singapore', 'Indonesia',
    'India', 'China', 'Mongolia', 'Myanmar', 'Laos',
    'Bhutan', 'Bangladesh', 'Nepal', 'Sri Lanka', 'Pakistan',
    'Kyrgyzstan', 'Australia', 'Russia', 'Tajikistan', 'Kazakhstan',
    'Uzbekistan', 'Turkmenistan', 'Iran', 'Oman', 'United Arab Emirates',
    'Kuwait', 'Iraq', 'Yemen', 'Azerbaijan', 'Georgia',
    'Turkey', 'Jordan', 'Israel', 'Lebanon', 'Syria',
    'Egypt', 'Sudan', 'Eritrea', 'Djibouti', 'Ethiopia',
    'Somalia', 'Kenya', 'Uganda', 'Tanzania', 'Malawi',
    'Mozambique', 'Zimbabwe', 'Zambia', 'Botswana', 'South Africa',
    'Namibia', 'Angola', 'Democratic Republic of the Congo', 'Central African Republic', 'Gabon',
    'Cameroon', 'Nigeria', 'Benin', 'Niger', 'Chad',
    'Mali', 'Togo', "Côte d'Ivoire", 'Liberia', 'Sierra Leone',
    'Guinea', 'Senegal', 'Mauritania', 'Western Sahara', 'Algeria',
    'Tunisia', 'Madagascar', 'United States', 'Canada', 'Mexico',
    'Argentina', 'Brazil', 'Colombia', 'Peru', 'Bolivia',
    'Uruguay', 'Paraguay', 'Chile', 'Puerto Rico', 'Cuba',
    'Suriname', 'Venezuela'
]
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# json파일 형태로 나라정보를 flask서버에 전송
@app.route('/get_country_info/<country_name>')
def get_country_info(country_name):
    return jsonify({
        'info': get_nation_info(country_name),
        'img_url': get_nation_img_url(country_name)
    })

# Flask 애플리케이션에서 모든 국가의 좌표 정보를 얻어오는 부분
@app.route('/get_all_countries_geo')
def get_all_countries_geo():
    all_countries_info = {}
    
    for country_name in countries:
        country_info = get_lat_lon_from_country(country_name)
        all_countries_info[country_name] = {
            'name': country_info['name'],
            'lat': country_info['lat'],
            'lng': country_info['lng']
        }

    return jsonify(countriesInfo=all_countries_info)
    
if __name__ == '__main__':
    app.run(debug=True)