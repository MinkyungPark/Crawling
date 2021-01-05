# JSON 특정 사이트 크롤링
# 검사 -> Network -> XHR -> F5누르기

# # Header
# Request URL: http://www.krei.re.kr:18181/chart/main_chart/index/kind/W/sdate/1972

# # Preview
# [{id: "2", date: "19720103", symbol: null, open: "0", close: "0", high: "0", low: "0",…},…]
# [0 … 9999]
# [0 … 99]
# 0: {id: "2", date: "19720103", symbol: null, open: "0", close: "0", high: "0", low: "0",…}
# id: "2"
# date: "19720103"
# symbol: null
# open: "0"
# close: "0"
# high: "0"
# low: "0"
# settlement: "59.4797"
# volume: "0"
# ....

from urllib.request import urlopen
import json

# url = 'http://www.krei.re.kr:18181/chart/main_chart/index/kind/W/sdate/2019-01-01/edate/2019-12-23'
# text = urlopen(url)
# print(text.read())

from_date = '2019-01-01'
to_date = '2019-12-23'
url = 'http://www.krei.re.kr:18181/chart/main_chart/index_grid_total/kind/S/sdate/'+from_date+'/edate/'+to_date
text = urlopen(url)

json_obj = json.load(text)

print(json_obj)