from urllib.request import urlopen
import bs4

html_str = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
"""
bs_obj = bs4.BeautifulSoup(html_str, 'html.parser')
li = bs_obj.find('li')
ul = bs_obj.find('ul')
lis = ul.findAll('li')
print(li.text)
print(ul.text)
print(li)
print(lis)
print(lis[0])
print(lis[1])

print()
print('--------------------class설정-------------------------')
html_str2 = '''
<html>
    <body>
        <ul class='greet'>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class='reply'>
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
    </body>
</html>
'''
bs_obj2 = bs4.BeautifulSoup(html_str2, 'html.parser')
ul = bs_obj2.find('ul', {'class':'reply'})
print(ul)
print(ul.text)

print()
print('--------------------속성별접근--------------------------')
html_str3 = '''
<html>
    <body>
        <ul class='ko'>
            <li>
                <a href='https://www.navercom/'>네이버</a>
            </li>
        <ul class='sns'>
            <li>
                <a href='https://www.facebookcom/>페이스북</a>
            </li>
        </ul>
    </body>
</html>'''
bs_obj3 = bs4.BeautifulSoup(html_str3, 'html.parser')
atag = bs_obj3.find('a')
print(atag)
print(atag['href']) # text말고 주소를 출력

print()
print('---------------------url로 테스트-----------------------')
url = 'https://news.naver.com/'
html = urlopen(url)
html_url_str = html.read()
bs_url_obj = bs4.BeautifulSoup(html_url_str, 'html.parser')
strong = bs_url_obj.find('strong')
strongs = bs_url_obj.find_all('strong')
print(strong.text) # 첫번째만 출력
for i in strongs:
    print(i.text)

print()
print('---------------------뉴스기사제목-----------------------')
ul_news = bs_url_obj.find('ul', {"class":"mlist2 no_bg"})
a_news = ul_news.find('a')
for i in a_news:
    print(a_news.text)

print()
print('---------------------naver-----------------------')
url2 = 'https://www.naver.com/'
html2 = urlopen(url2)
html_url_str2 = html2.read()
bs_url_obj2 = bs4.BeautifulSoup(html_url_str2, 'html.parser')
ul = bs_url_obj2.find('ul', {"class":"an_l"})
span = ul.findAll('span',{"class":"an_txt"})
print(span)
print()
for i in span:
    print(i.text)

