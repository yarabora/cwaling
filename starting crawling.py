# 크롤링 시작
import time
from selenium import webdriver
#크롬 브라우저 열기
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.instagram.com')
time.sleep(3)

driver.get('https://www.instagram.com')
time.sleep(3)
email = 'hahah425@nate.com'
input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
input_id.clear()
input_id.send_keys(email)

password = '인스타그램 로그인 비번'
input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
input_pw.clear()
input_pw.send_keys(password)
input_pw.submit()

time.sleep(5)

word = input("검색어를 입력하세요 : ")
word = str(word)
url = insta_searching(word)
