from urllib.request import urlopen
from urllib.parse import quote
import urllib
from bs4 import BeautifulSoup
import pandas as pd

# CSV 파일에서 국가 정보 읽기
df = pd.read_csv('./data/country.csv')

def get_nation_info(name):
    for nation_name in df['나라']:
        if name == nation_name:
            encoded_name = quote(nation_name)  # URL에 사용 가능한 형태로 인코딩
            html2 = urlopen("https://ko.wikipedia.org/wiki/" + encoded_name)
            bsObject2 = BeautifulSoup(html2, "html.parser")
            info_code = bsObject2.select('div.mw-parser-output > p')
            # 개별 p 태그의 텍스트를 리스트로 저장
            nation_info = [tag.get_text() for tag in info_code]
            
            # 리스트 내 문자열을 합쳐서 반환
            return '\n'.join(nation_info)

def get_nation_img_url(name):
    for nation_name in df['나라']:
        try:
            encoded_name = quote(nation_name)  # URL에 사용 가능한 형태로 인코딩
            html2 = urlopen("https://ko.wikipedia.org/wiki/" + encoded_name)
            bsObject2 = BeautifulSoup(html2, "html.parser")
            
            # 이미지 태그를 찾는 CSS 선택자
            img_tag = bsObject2.select_one('div.mw-parser-output img')
            
            # 이미지 태그가 존재하는 경우에만 URL 반환
            if img_tag:
                img_url = img_tag['src']
                return img_url
            else:
                return "이미지를 찾을 수 없습니다."
        except urllib.error.HTTPError as e:
            print(f"HTTP Error for {nation_name}: {e}")
            return "이미지를 찾을 수 없습니다."

# # ImageURL 열만 선택하여 CSV 파일로 저장
# df['ImageURL'] = df['나라'].apply(lambda x: get_nation_img_url(x))

# # 다시 원래 DataFrame을 CSV 파일로 저장
# df.to_csv('./data/country.csv', index=False)