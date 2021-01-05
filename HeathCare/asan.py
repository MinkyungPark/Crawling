import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
import pandas as pd
import re

df = pd.read_csv('disease.csv', names=['names', 'origin'], encoding='utf-8') # 충치뺌

disease_list = []
for data in df['names']:
    disease_list.append(data)

print(disease_list)

path = 'C://chromedriver'
driver = webdriver.Chrome(path)

# search_box.submit()
# driver.implicitly_wait(3)

result = []
# result = [[검색용어, 검색된용어, 요약, 자세한내용], [검색용어, 검색된용어, 요약, 자세한내용],...]

for disease in disease_list:
    driver.get('http://www.amc.seoul.kr/asan/healthinfo/disease/diseaseSubmain.do')
    search_box = driver.find_element_by_name('searchKeyword')
    search_box.send_keys(disease)
    btn = driver.find_element_by_xpath('//*[@id="diseaTab"]/div[1]/div/dl/dd[2]/a').click()



    lis = driver.find_elements_by_xpath('//*[@id="listForm"]/div/div/ul/li')

    try:
        for i in range(len(lis)):
            tmp = []
            tmp.append(disease)
            
            divs = driver.find_elements_by_xpath('//*[@id="listForm"]/div/div/ul/li')
            searched = divs[i].find_element_by_tag_name('a')
            tmp.append(searched.text)

            summary = divs[i].find_element_by_tag_name('dd')
            tmp.append(summary.text)

            searched.click()

            try:
                lis2 = driver.find_elements_by_xpath('//*[@id="content"]/div[2]/div[1]/div[2]/dl/dt')
                for i in range(len(lis2)):
                    dts = driver.find_elements_by_xpath('//*[@id="content"]/div[2]/div[1]/div[2]/dl/dt')
                    dds = driver.find_elements_by_xpath('//*[@id="content"]/div[2]/div[1]/div[2]/dl/dd')
                    title = dts[i].text
                    contents = dds[i].text
                    tmp.append(title)
                    tmp.append(contents)
                    result.append(tmp)
                    
            except NoSuchElementException:
                print('증상 데이터 없음')
                continue

            driver.back()


    except NoSuchElementException:
        print(disease, end='')
        print(' 데이터 없음')
        continue



sub_result = []
for line in result:
    tmp = []
    for word in line:
        word = re.sub('[\n, \t, \r]', ' ', word)
        tmp.append(word)
    sub_result.append(tmp)


save = pd.DataFrame(sub_result)
save.to_csv('아산병원증상크롤링.csv', encoding='utf-8')