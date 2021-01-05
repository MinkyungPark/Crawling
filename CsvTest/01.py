import csv, codecs

with codecs.open('test.csv', 'w', 'euc_kr') as fp:
    writer = csv.writer(fp, delimiter=',', quotechar='"')
    writer.writerow(['ID', '이름', '가격'])
    writer.writerow(['1000', 'SD 카드', '30000'])
    writer.writerow(['1001', '키보드', '21000'])
    writer.writerow(['1002', '마우스', '15000'])

filename = 'test.csv'
fp = codecs.open(filename, 'r', 'euc_kr') # csv생성 및 쓰기
# 한줄 씩 읽어들이기
reader = csv.reader(fp, delimiter=',', quotechar='"')
for cells in reader:
    print(cells[0], cells[1], cells[2])