import openpyxl

filename = 'population.xlsx'
book = openpyxl.load_workbook(filename)
sheet = book.worksheets[0]
data = []

for row in sheet.rows:
    data.append([row[0].value, row[9].value])

# clean data(헤더, 연도, 계 제거)
del data[0]
del data[1]
del data[2]

# 데이터 인구순 정렬
data = sorted(data, key=lambda x:x[1])
print(data)

# 하위 5위 출력
for i, a in enumerate(data):
    if(i >= 5): break
    print(i+1, a[0], a[1])

# 활성화된 시트 추출
sheet = book.active

# 서울을 제외한 인구를 구해서 쓰기
for i in range(0, 9):
    total = int(sheet[str(chr(i + 66)) + '3'].value)
    seoul = int(sheet[str(chr(i + 66)) + '4'].value)
    output = total - seoul
    print('서울 제외 인구=', output)
    # 쓰기
    sheet[str(chr(i + 66)) + '21'] = output
    cell = sheet[str(chr(i + 66)) + '21']
    cell.font = openpyxl.styles.Font(size=14, color='FF0000')
    cell.number_format = cell.number_format

filename = 'population2.xlsx'
book.save(filename)
print('ok')
