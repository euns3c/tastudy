from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import pywinauto
import time, sys

# from bs4 import BeautifulSoup
# from urllib.request import urlopen

driver = webdriver.Chrome('C:/chromedriver.exe')
url = 'https://www.tistory.com/'
driver.get(url)
time.sleep(1)


# 티스토리 로그인 함수
def login(id, pw):
    driver.find_element_by_link_text('로그인하기').click()
    driver.find_element_by_name('loginId').send_keys(id)
    driver.find_element_by_name('password').send_keys(pw)
    driver.find_element_by_name('password').send_keys(Keys.ENTER)


login('eunsk31@daum.net', '')


# 이미지 첨부 함수
def upload_img(filepath):
    # '열기' 타이틀 windows dialog에 커넥
    app = pywinauto.application.Application().connect(title_re="열기")
    # 함수 인자로 받은 파일 경로 입력
    app.열기.Edit.set_edit_text(filepath)
    # [열기] 버튼 클릭
    app.열기.Button.click()


# 블로그 포스팅 함수
def posting():
    driver.find_element_by_css_selector('.thumb_profile').click()
    driver.find_element_by_link_text('쓰기').click()
    driver.find_element_by_css_selector('.textarea_tit').send_keys("제목을 입력합니다.")

    # sys.exit()  # 프로그램 종료
    # iframe : html 안에 또 다른 html이 있는 것
    # iframe 위치 지정. (iframe을 감싸고 있는 div 하위에 iframe이 있음)
    iframe = driver.find_element_by_css_selector(
        '.mce-edit-area.mce-container.mce-panel.mce-stack-layout-item.mce-last iframe')
    # iframe으로 이동
    driver.switch_to.frame(iframe)
    # iframe 안의 콘텐츠 작성 영역(p 태그)에 내용 입력
    driver.find_element_by_tag_name('p').send_keys("내용을 입력합니다.")
    # 기존 프레임으로 이동
    driver.switch_to.default_content()

    driver.find_element_by_id('mceu_0-open').click()  # 첨부 클릭
    driver.find_element_by_id('mceu_32').click()  # 사진 클릭
    time.sleep(3)

    # pywinauto 라이브러리로 windows dialog 제어
    # 파이썬에서 \\ = \
    upload_img("C:\\test_img.png")

    # 태그1-3 입력
    driver.find_element_by_name('tagText').send_keys("태그1" + Keys.ENTER + "태그2" + Keys.ENTER + "태그3" + Keys.ENTER)
    # [완료] 버튼 클릭
    driver.find_element_by_css_selector('.btn.btn-default').click()
    time.sleep(3)

    if driver.find_element_by_id('open0').is_selected():
        print("비공개")
    elif driver.find_element_by_id('open15').is_selected():
        print("공개(보호)")
    else:
        print("공개")

    print(driver.find_element_by_id('open20').get_attribute('value'))
    print(driver.find_element_by_id('open15').get_attribute('value'))
    print(driver.find_element_by_css_selector('.btn.btn-default').is_enabled())

    # 포스팅 범위 '공개' 설정
    driver.find_elements_by_css_selector('.form-radio.klink-linknew')[0].click()

    # [완료 > 두번째 저장] 클릭
    # [완료]와 [두번째 저장] 버튼 클래스가 동일해서 [두번째 저장]을 클릭하려면 배열 요소를 명시해줘야 함
    driver.find_elements_by_css_selector('.btn.btn-default')[1].click()


posting()
