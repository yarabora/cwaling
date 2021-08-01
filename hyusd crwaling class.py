from selenium import webdriver
from time import sleep

# 크롬 웹드라이버 경로 설정
driver = webdriver.Chrome('C:\\webdriver\\chromedriver.exe')
# # 네이버  로그인 화면 접속
driver.get('https://nid.naver.com/nidlogin.login')
sleep(3)
driver.find_element_by_id('id').send_keys('lalala_0425')
sleep(3)
driver.find_element_by_id('pw').send_keys('2018116a')
driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/form/fieldset/input').click()

# 두번째
driver.find_element_by_id('id').send_keys('lalala_0425')
sleep(3)
driver.find_element_by_id('pw').send_keys('2018116a')
driver.find_element_by_id('captcha').send_keys('1')
sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/fieldset/input').click()



