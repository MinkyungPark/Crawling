# 함수 적용 100개 검색 내용 출력
# display 는 최대 100

import requests
from urllib.parse import urlparse

def get_api_result(keyword, display):
    url = 'https://openapi.naver.com/v1/search/blog?query=' + keyword + str(display)
    result = requests.get(urlparse(url).geturl(),
                           headers={'X-Naver-Client-Id':'1IBRj5i3SPdFnFP4550z',
                           'X-Naver-Client-Secret':'LsY2HHc8r4'})
    return result.json()

json_obj = get_api_result('광운대학교', 100)

print(json_obj)