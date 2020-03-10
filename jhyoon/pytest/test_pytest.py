#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import sys
import os
import getpass
import time
import pytest
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from path import path

id = 'input id'
pw = 'input pw'

@pytest.fixture()
def setup():
    global 드라이버
    options = Options()
    options.headless = False
    드라이버 = webdriver.Chrome(executable_path="..\\chromedriver.exe", options=options)
    드라이버.implicitly_wait(5)


def test_login(setup):
    드라이버.get(path.티스토리)
    드라이버.find_element_by_link_text('로그인하기').click()
    드라이버.find_element_by_name('loginId').send_keys(id)
    드라이버.find_element_by_name('password').send_keys(pw)
    드라이버.find_element_by_name('password').send_keys(Keys.ENTER)

def test_profile_view():
    try:
        드라이버.find_element_by_xpath(path.프로필아이콘)

    except Exception as ex:
        print('오류가 발생 하였습니다. 내용을 확인 하세요. > {}'.format(ex))
        
        if 드라이버.find_element_by_xpath('//a[@class="btn_basic btn_primary "]'):
            print('웹에서 로그인 하신 후, 하기 설정 후 재 시도 하십시요.')
            print('[계정관리 > 보안 > 로그인 기기관리]에서 - 모든기기에서 로그인을 허용합니다 - ')

def test_profile_click():
    드라이버.find_element_by_xpath(path.프로필아이콘).click()

def test_write_click():
    드라이버.find_element_by_xpath(path.블로그글쓰기).click()

def test_write_page_view():
    드라이버.find_element_by_xpath(path.카테고리_셀렉트)
    드라이버.find_element_by_xpath(path.제목_인풋)
    iframe = 드라이버.find_element_by_xpath(path.내용_타이틀)
    드라이버.switch_to.frame(iframe)
    드라이버.find_element_by_xpath(path.내용_텍스트박스)
    드라이버.switch_to.default_content()
    드라이버.find_element_by_xpath(path.태그)

def test_write_page_wrtie():
    제목_내용 = '제목 입니다. 작성 시간은 {}'.format(time.strftime("%H:%M:%S", time.localtime(time.time())))
    본문_내용 = '가나다라마바사아자차카타파하'
    태그_내용 = '하나다루루루'

    드라이버.find_element_by_xpath(path.제목_인풋).send_keys('{}'.format(제목_내용))
    iframe = 드라이버.find_element_by_xpath(path.내용_타이틀)
    드라이버.switch_to.frame(iframe)
    드라이버.find_element_by_xpath(path.내용_텍스트박스).send_keys('{}'.format(본문_내용))
    드라이버.switch_to.default_content()
    드라이버.find_element_by_xpath(path.태그).send_keys('{}'.format(태그_내용))
    드라이버.find_element_by_xpath(path.태그).send_keys(Keys.ENTER)

def test_write_page_save():
    드라이버.find_element_by_xpath(path.완료).click()
    드라이버.find_element_by_xpath(path.비공개저장).click()

def test_close():
    드라이버.quit()