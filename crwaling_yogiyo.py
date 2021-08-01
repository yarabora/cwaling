from selenium import webdriver
from bs4 import BeautifulSoup
from time import time
import re
import time


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


###  크롤링 시작
#크롬 브라우저 열기
driver = webdriver.Chrome('C:\\webdriver\\chromedriver.exe')

driver.get('https://www.yogiyo.co.kr/')
driver.get("https://www.yogiyo.co.kr/mobile/#/452598/")
driver.maximize_window()
time.sleep(3)

