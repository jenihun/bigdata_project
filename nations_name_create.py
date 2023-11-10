import pycountry

def get_popular_countries(num_countries=100):
    # 인기 있는 나라들을 가져오기
    popular_countries = list(pycountry.countries)[:num_countries]
    
    # 나라 이름 출력
    for country in popular_countries:
        print(country.name)

# 100개의 인기 있는 나라 출력
get_popular_countries(100)