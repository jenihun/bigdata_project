import json

# JSON 파일 읽기
with open('C:/bigdata_project/data/all_countries_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 영어 국가 이름 리스트
eng_names = ['United Kingdom', 'France', 'Germany', 'Italy', 'Spain', 'Ireland', 'Portugal', 'Belgium', 'Netherlands', 'Denmark', 'Norway', 'Sweden', 'Finland', 'Poland', 'CzechRepublic', 'Austria', 'Croatia', 'Slovakia', 'Hungary', 'Serbia', 'Greece', 'Lithuania', 'Estonia', 'Latvia', 'Belarus', 'Ukraine', 'Romania', 'Bulgaria', 'Moldova', 'Korea', 'Saudi Arabia', 'Japan', 'Philippines', 'Singapore', 'Indonesia', 'India', 'China', 'Mongolia', 'Myanmar', 'Laos', 'Bhutan', 'Bangladesh', 'Nepal', 'Sri Lanka', 'Pakistan', 'Kyrgyzstan', 'Australia', 'Russia', 'Tajikistan', 'Kazakhstan', 'Uzbekistan', 'Turkmenistan', 'Iran', 'Oman', 'United Arab Emirates', 'Kuwait', 'Iraq', 'Yemen', 'Azerbaijan', 'Georgia', 'Turkey', 'Jordan', 'Israel', 'Lebanon', 'Syria', 'Egypt', 'Sudan', 'Eritrea', 'Djibouti', 'Ethiopia', 'Somalia', 'Kenya', 'Uganda', 'Tanzania', 'Malawi', 'Mozambique', 'Zimbabwe', 'Zambia', 'Botswana', 'South Africa', 'Namibia', 'Angola', 'Democratic Republic of the Congo', 'Central African Republic', 'Gabon', 'Cameroon', 'Nigeria', 'Benin', 'Niger', 'Chad', 'Mali', 'Togo', "Côte d'Ivoire", 'Liberia', 'Sierra Leone', 'Guinea', 'Senegal', 'Mauritania', 'Western Sahara', 'Algeria', 'Tunisia', 'Madagascar', 'UnitedStates', 'Canada', 'Mexico', 'Argentina', 'Brazil', 'Colombia', 'Peru', 'Bolivia', 'Uruguay', 'Paraguay', 'Chile', 'PuertoRico', 'Cuba', 'Suriname', 'Venezuela']

# 'eng_name' 필드 추가
for i, country in enumerate(data):
    country['eng_name'] = eng_names[i]

# 업데이트된 데이터를 JSON으로 변환
json_data = json.dumps(data, indent=2, ensure_ascii=False)

# 새로운 JSON 파일로 저장
with open('C:/bigdata_project/data/all_countries_data.json', 'w', encoding='utf-8') as file:
    file.write(json_data)