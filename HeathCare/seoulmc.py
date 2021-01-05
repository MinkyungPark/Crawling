import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
import pandas as pd
import re

df = pd.read_csv('disease.csv', names=['names', 'origin'], encoding='utf-8')

disease_list = []
for data in df['names']:
    disease_list.append(data)

print(disease_list)

path = 'C://chromedriver'
driver = webdriver.Chrome(path)

# search_box.submit()
# driver.implicitly_wait(3)

result = []
# result = [[질병명, 증상, 내용], [질병명, 증상, 내용],...]

for disease in disease_list:
    driver.get('https://www.seoulmc.or.kr/site/board/medicalguide/medicalInfo/dictionary/healthSearchList.do?menucdv=04010000')
    search_box = driver.find_element_by_name('key01')
    search_box.send_keys(disease)
    btn = driver.find_element_by_xpath('//*[@id="sitemesh_content"]/div[2]/div[1]/div[2]/fieldset/a').click()

    tdss = driver.find_elements_by_xpath('//*[@id="sitemesh_content"]/div[3]/table/tbody/tr/td/a')
    
    # len(tdss) 7

    try:
        for i in range(len(tdss)):
            tds = driver.find_elements_by_xpath('//*[@id="sitemesh_content"]/div[3]/table/tbody/tr/td/a')

            tds[i].click()

            dis_name = driver.find_element_by_xpath('//*[@id="sitemesh_content"]/div[1]/table/tbody/tr/td/div/dl/dt')
            title = driver.find_element_by_xpath('//*[@id="sitemesh_content"]/div[1]/table/tbody/tr/td/div/dl/dd[5]')
            contents = driver.find_element_by_xpath('//*[@id="sitemesh_content"]/div[1]/table/tbody/tr/td/div/dl/dd[6]')

            tmp = []
            tmp.append(disease)
            tmp.append(dis_name.text)
            tmp.append(title.text)
            tmp.append(contents.text)
            result.append(tmp)
            
            driver.back()

    except NoSuchElementException:
        print(disease, end='')
        print('데이터 없음')
        continue

sub_result = []
for line in result:
    tmp = []
    for word in line:
        word = re.sub('[\n, \t, \r]', ' ', word)
        tmp.append(word)
    sub_result.append(tmp)


save = pd.DataFrame(sub_result)
save.columns = ['search','searched','category','contents']
save.to_csv('서울의료원증상크롤링.csv', encoding='utf-8')