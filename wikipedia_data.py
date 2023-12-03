from urllib.request import urlopen
from urllib.parse import quote
import urllib
from bs4 import BeautifulSoup
import pandas as pd
import re

# CSV 파일에서 데이터프레임 읽기
df = pd.read_csv('./data/country.csv')

# '나라'와 'ImageURL' 열 선택
selected_columns = ['나라']

# 선택한 열을 사용하여 새로운 데이터프레임 생성
selected_df = df[selected_columns]

def get_nation_currency(name):
    for nation_name in selected_df['나라']:
        if name == nation_name:
            encoded_name = quote(nation_name)  # URL에 사용 가능한 형태로 인코딩
            html = urlopen("https://ko.wikipedia.org/wiki/" + encoded_name)
            bsObject = BeautifulSoup(html, "html.parser")
            
            # 통화 정보를 찾기 위해 테이블 전체를 선택
            info_table = bsObject.select_one('#mw-content-text > div.mw-content-ltr.mw-parser-output table.infobox.geography.vcard')
            
            # 테이블이 존재하지 않으면 통화 정보가 없음을 반환
            if not info_table:
                return "통화 정보 없음"
            
            # 테이블의 모든 행(tr)을 가져와서 반복
            for row in info_table.select('tr'):
                # 현재 행에서 텍스트가 '통화'인 셀(td 또는 th)을 찾음
                currency_cell = row.find('td', text='통화') or row.find('th', text='통화')
                
                # 통화를 찾은 경우
                if currency_cell:
                    # 다음 형제인 셀(td 또는 th)의 값을 가져옴
                    currency_value = currency_cell.find_next('td') or currency_cell.find_next('th')
                    
                    # 값을 찾은 경우 반환
                    if currency_value:
                        return currency_value.get_text(strip=True)
                    
def get_nation_religion(name):
    for nation_name in selected_df['나라']:
        if name == nation_name:
            encoded_name = quote(nation_name)  # URL에 사용 가능한 형태로 인코딩
            html = urlopen("https://ko.wikipedia.org/wiki/" + encoded_name)
            bsObject = BeautifulSoup(html, "html.parser")
            
            # 테이블 전체 선택
            info_table = bsObject.select_one('#mw-content-text > div.mw-content-ltr.mw-parser-output table.infobox.geography.vcard')
            
            # 테이블이 존재하지 않으면 종교 정보가 없음을 반환
            if not info_table:
                return ["종교 정보 없음"]
            
            # 테이블의 모든 행(tr)을 가져와서 반복
            for row in info_table.select('tr'):
                # 현재 행에서 텍스트가 '종교'인 셀(td 또는 th)을 찾음
                religion_cell = row.find('td', text='종교') or row.find('th', text='종교')
                
                # 종교를 찾은 경우
                if religion_cell:
                    # 다음 형제인 셀(td 또는 th)의 값을 가져옴
                    religion_value = religion_cell.find_next('td') or religion_cell.find_next('th')
                    
                    # 값을 찾은 경우 리스트로 반환
                    if religion_value:
                        # 각 값을 리스트에 추가, 제거 할 때 정규표현식 사용
                        religions = [re.sub(r'\[[0-9]+\]', '', rel.text.strip()) for rel in religion_value.find_all('a')]
                        
                        # 제거한 후 빈 문자열을 필터링
                        religions = list(filter(None, religions))
                        
                        return religions
                        
            # 종교 정보가 없는 경우
            return ["종교 정보 없음"]
        
def get_population_after_year(name):
    for nation_name in selected_df['나라']:
        if name == nation_name:
            encoded_name = quote(nation_name)  # URL에 사용 가능한 형태로 인코딩
            html = urlopen("https://ko.wikipedia.org/wiki/" + encoded_name)
            bsObject = BeautifulSoup(html, "html.parser")
            
            # 테이블 전체 선택
            info_table = bsObject.select_one('#mw-content-text > div.mw-content-ltr.mw-parser-output table.infobox.geography.vcard')
            
            # 테이블이 존재하지 않으면 정보가 없음을 반환
            if not info_table:
                return "정보 없음"
            
            # 테이블의 모든 행(tr)을 가져와서 반복
            for row in info_table.select('tr'):
                # 현재 행에서 텍스트가 '인구'인 셀(td 또는 th)을 찾음
                population_cell = row.find('th', text='인구')
                
                # 인구를 찾은 경우
                if population_cell:
                    # a 태그를 찾음
                    a_tag = population_cell.find('a')
                    
                    # a 태그가 존재하면 다음 형제인 td의 값을 가져옴
                    if a_tag:
                        population_value = a_tag.find_next('td')
                        
                        # 값을 찾은 경우
                        if population_value:
                            # 괄호와 내용을 제거하고 숫자와 콤마만 남김
                            population_text = re.sub(r'\([^)]*\)', '', population_value.get_text())
                            
                            # 특수 기호 제거
                            population_text = re.sub(r'[^\d만,]', '', population_text)
                            
                            # 만이 있으면 '만'을 포함하여 반환
                            if '만' in population_text:
                                return population_text + '명'
                            else:
                                return population_text + '명'
            
            # 정보가 없는 경우
            return "정보 없음"
        
def get_nation_info(name):
    for nation_name in selected_df['나라']:
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
    for nation_name in selected_df['나라']:
        if name == nation_name:
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
