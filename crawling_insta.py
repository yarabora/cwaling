from selenium import webdriver
from bs4 import BeautifulSoup
from time import time
import re
import time


# 함수 정의: 검색어 조건에 따른 url생성
def insta_searching(word):
    url = "https://www.instagram.com/explore/tags/" + str(word)
    return url

# 열린 페이지에서 첫번째 게시물 클릭
def select_first(driver):
    driver.find_element_by_css_selector('._9AhH0').click()

    time.sleep(3)
# 본문 내용, 작성일자, 좋아요 수, 위치정보, 해시태그 가져오기
def get_content(driver):
    html = driver.page_source
    soup = BeautifulSoup(html,'lxml')
    # 본문내용
    try:
        content = soup.select('div.C4VMK > span')[0].text
    except:
        content = ' '
    # 해시태그
    tags = re.findall(r'#[^\s#,\\]+', content)
    # 작성일자
    date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10]

    # 좋아요
    try:
        like = soup.select('div.Nm9Fw')[0].text[4:-1]
    except:
        like = 0
        #위치
    try:
        place = soup.select('div.M30cS')[0].text

    except:
        place = ''
    data = [content, date, like, place, tags]
    return data


# 첫 번재 게시물 클릭 후 다음 게시물 클릭
def move_next(driver):
    right = driver.find_element_by_css_selector ('a.coreSpriteRightPaginationArrow')
    right.click()
    time.sleep(3)


# 크롤링 시작
#크롬 브라우저 열기
driver = webdriver.Chrome('C:\\webdriver\\chromedriver.exe')

driver.get('https://www.instagram.com')
time.sleep(3)

# 인스타 그램 로그인을 위한 계정 정보

email = 'hahah425@nate.com'
input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
input_id.clear()
input_id.send_keys(email)

password = 'hu2018116A!'
input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
input_pw.clear()
input_pw.send_keys(password)
input_pw.submit()

time.sleep(5)

import random
# 로그인설정 나중에 하기
xpath1 = '//*[@id="react-root"]/section/main/div/div/div/div/button'
driver.find_element_by_xpath(xpath1).click()
time.sleep(random.uniform(2,4))
# 알림설정 나중에하기
xpath2 = '/html/body/div[4]/div/div/div/div[3]/button[2]'
driver.find_element_by_xpath(xpath2).click()
time.sleep(random.uniform(2,4))

# 게시물을 조회할 검색 키워드 입력 요청
word = input("검색어를 입력하세요 : ")
word = str(word)
url = insta_searching(word)
# 검색 결과 페이지 열기
driver.get(url)
time.sleep(3)
# 첫 번째 게시물 클릭
select_first(driver)

#데이터 수집 시작
results = []
target = 5
for i in range(target):
    try:
        data = get_content(driver)
        results.append(data)
        move_next(driver)
    except:
        time.sleep(2)
        move_next(driver)
    print(results[:2])

import pandas as pd
results_df = pd.DataFrame(results)
results_df.columns = ['content','data','like','place','tags']
results_df.to_excel(r'C:\devel\Funnyblog_bora\test1.xlsx')