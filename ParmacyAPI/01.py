# 공공데이터 약국조회서비스 이용
# 개발가이드의 파라미터 값 조회해서 오후 9시 이후에 여는 약국 조회

from urllib.parse import quote
import requests
import bs4

endpoint = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
serviceKey = '6iRbVHH7LdTIkiGBve1cJn5abJR2TULQhwfLOd4ku7P5iISHj98r48EimGYPVhJdd0i49r9UNxhio%2F3QMZQH3g%3D%3D'

Q0 = quote('서울특별시')  # quote 인코딩하는 함수
Q1 = quote('강남구')
QT = '1'
QN = quote('삼성약국')
ORD = 'NAME'
pageNo = '1'
startPage = '1'
numOfRows = '5000'
pageSize = '10'

# paramset = 'serviceKey=' + serviceKey + '&Q0=' + Q0 + '&Q1=' + Q1 + '&QT=' + QT \
#            + '&QN=' + QN + '&ORD=' + ORD + '&pageNo=' + pageNo \
#            + '&startPage=' + startPage + 'numOfRows=' + numOfRows \
#            + '&pageSize=' + pageSize

paramset = 'serviceKey=' + serviceKey + '&Q0=' + Q0 + '&ORD=' + ORD + '&pageNo=' + pageNo \
           + '&startPage=' + startPage + '&numOfRows=' + numOfRows \
           + '&pageSize=' + pageSize

# find()는 html(xml)을 작업.
# json은 ['']이용

url = endpoint + paramset
print(url)
result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, 'html.parser')
items = bs_obj.find_all("item")

# for item in items:
#     tagged_item = item.find('dutyname')
#     print(tagged_item)

# count = 0
# for item in items:
#     tagged_item = item.find('dutytime1c')
#     if(tagged_item != None):
#         close_time = int(tagged_item.text)
#         if(close_time > 2100):
#             count += 1
#
# print('서울특별시 내 월요일 9시 이후까지 하는 약국의 수 : ' + str(count))

dutyname = []
for item in items:
    tagged_item = item.find('dutytime1c')
    tagged_item_name = item.find('dutyname')
    if(tagged_item != None):
        close_time = int(tagged_item.text)
        if(close_time > 2100):
            dutyname.append(tagged_item_name.text)

for i in dutyname:
    print(i)