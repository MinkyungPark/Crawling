import requests
from urllib.parse import urlparse

keyword = '광운대'
url = 'https://openapi.naver.com/v1/search/blog?query=' + keyword + '&display=100'
result = requests.get(urlparse(url).geturl(),
                       headers={'X-Naver-Client-Id':'1IBRj5i3SPdFnFP4550z',
                       'X-Naver-Client-Secret':'LsY2HHc8r4'})

#json_obj = result.json()
# for item in json_obj['items']:
#     print(item)

json_obj = result.json()

for item in json_obj['items']:
    print('Title : ' + item['title'])
    print('Without <b> : ' + item['title'].replace('<b>','').replace('</b>',''))
    print('Link : ' + item['link'])
    print('Description : ' + item['description'])

# json viewr로 전체 json 구조 파악하기


print('------------------------------------------------------------------------')
print('------------------------------------------------------------------------')
# 검색 횟수 범위 조절
# url = 'https://openapi.naver.com/v1/search/blog?query=' + keyword 일때
print('display : ' + str(json_obj['display']))
print('start : ' + str(json_obj['start']))
print('items : ' + str(len(json_obj['items'])))
# display : 10
# start : 1
# items : 10

# https://developers.naver.com/docs/search/blog/ 에서 출력결과 확인
# url = 'https://openapi.naver.com/v1/search/blog?query=' + keyword + '&display=100' 일때
# display : 100
# start : 1
# items : 100