from urllib.request import urlopen
from urllib.parse import quote
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
        if name == nation_name:
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

# from urllib.request import urlopen
# from urllib.parse import quote
# from bs4 import BeautifulSoup
# import pandas as pd

# html1 = urlopen("https://ko.wikipedia.org/wiki/%EB%82%98%EB%9D%BC_%EC%9D%B4%EB%A6%84%EC%88%9C_%EC%88%98%EB%8F%84_%EB%AA%A9%EB%A1%9D")
# bsObject = BeautifulSoup(html1, "html.parser")

# # 수정된 선택자 사용
# li_code = bsObject.select('div.mw-parser-output ul li')

# ulli_total = []
# for c in range(0, len(li_code)):
#     ulli_total.append(li_code[c].get_text())

# # "나라, 수도"로 정렬시키기
# data = []
# for a in range(0, len(ulli_total)):
#     if ' - ' in ulli_total[a]:
#         data.append(ulli_total[a].split(' - '))
        
# countries = []
# for item in data:
#     countries.append(item[0])

# # 데이터프레임 생성
# df = pd.DataFrame({'Country': countries})

# # 각 나라에 대한 정보 및 이미지 URL을 추가
# df['Info'] = df['Country'].apply(lambda x: get_nation_info(x))
# df['ImageURL'] = df['Country'].apply(lambda x: get_nation_img_url(x))

# # CSV 파일로 내보내기
# df.to_csv('nations_info.csv', index=False)