# http://www.krei.re.kr:18181/new_sub01 밀가격 가져오기 크롤링

from urllib.request import urlopen
from urllib.parse import urlparse
import json

from_date = '2019-11-01'
to_date = '2019-12-20'
url = 'http://www.krei.re.kr:18181/chart/main_chart/index/kind/W/sdate/'+from_date+'/edate/'+to_date
result = urlopen(url)

json_obj = json.load(result)

print(json_obj)

for item in json_obj:
    id = item['id']
    date = item['date']
    # symbol = item['symbol']
    open = item['open']
    close = item['close']
    high = item['high']
    low = item['low']
    settlement = item['settlement']
    volume = item['volume']
    print(id + '@' + date + '@' + settlement)
