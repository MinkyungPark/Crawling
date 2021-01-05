# 공공기관 API 이용

# 매뉴얼 json요청 url에 SERVICE KEY 내꺼 넣기
# http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaCode?ServiceKey=6iRbVHH7LdTIkiGBve1cJn5abJR2TULQhwfLOd4ku7P5iISHj98r48EimGYPVhJdd0i49r9UNxhio%2F3QMZQH3g%3D%3D&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=TestApp&_type=json
# http://api.visitkorea.or.kr/openapi/service
# 활용 메뉴얼 활용

# 한국관광공사 API 14p 활용

import requests
import bs4

endpoint = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?'
serviceKey = '6iRbVHH7LdTIkiGBve1cJn5abJR2TULQhwfLOd4ku7P5iISHj98r48EimGYPVhJdd0i49r9UNxhio%2F3QMZQH3g%3D%3D'

numOfRows = '10'
pageSize = '1'
pageNo = '1'
MobileOS = 'ETC'
MobileApp = 'AppTest'
arrange = 'A'
contentTypeID = '15'
areaCode = '1'
sigunguCode = '3'
listYN = 'Y'

paramset = 'serviceKey=' + serviceKey + '&numOfRows=' + numOfRows + '&pageSize=' \
           + pageSize + '&pageNo=' + pageNo + '&MobileOS=' + MobileOS + '&MobileApp=' + MobileApp \
           + '&arrange=' + arrange + '&contentTypeId=' + contentTypeID + '&areaCode=' + areaCode \
           + '&sigunguCode=' + sigunguCode + '&listYN=' + listYN + '&_type=json'

url = endpoint + paramset
print(url)
result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, 'html.parser')
print(bs_obj)

# viewer로 아이템 확인.
# 홈페이지에서 실행->미리보기 기능 활용
