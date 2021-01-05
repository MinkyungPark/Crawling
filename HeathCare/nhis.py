import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
import pandas as pd
import re

df = pd.read_csv('disease2.csv', names=['names', 'origin'], encoding='utf-8') # 충치뺌

disease_list = []
for data in df['names']:
    disease_list.append(data)

print(disease_list)

path = 'C://chromedriver'
driver = webdriver.Chrome(path)

# search_box.submit()
# driver.implicitly_wait(3)

result = []
# result = [[검색용어, 질병및카테고리, 내용], [검색용어, 질병및카테고리, 내용],...]

for disease in disease_list:
    driver.get('https://hi.nhis.or.kr/cc/ggpcc001/ggpcc001_m01.do')
    search_box = driver.find_element_by_name('inputsearchWord')
    search_box.send_keys(disease)
    btn = driver.find_element_by_xpath('//*[@id="search_word"]/div/a').click()

    trs = driver.find_elements_by_xpath('//*[@id="contents"]/div[2]/table/tbody/tr/td/a')

    try:
        for i in range(len(trs)):
            tds = driver.find_elements_by_xpath('//*[@id="contents"]/div[2]/table/tbody/tr/td/a')
            if '개요' in tds[i].text:
                # print(tds[i].text)
                tds[i].click()
                uls = driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/ul/li/a')

                try:
                    for i in range(len(uls)):
                        lis = driver.find_elements_by_xpath('//*[@id="contents"]/div[1]/ul/li/a')
                        if '증상' in lis[i].text:
                            # print(lis[i].text)
                            lis[i].click()

                            category = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/table/thead/tr/th')
                            contents = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/table/tbody/tr[2]/td')
                            
                            tmp = []
                            tmp.append(disease)
                            tmp.append(category.text)
                            tmp.append(contents.text)
                            result.append(tmp)

                            driver.back()
                
                except NoSuchElementException:
                    print('검색 결과 없음')
                    continue

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
save.columns = ['search', 'category','contents']
save.to_csv('건강IN증상크롤링.csv', encoding='utf-8')