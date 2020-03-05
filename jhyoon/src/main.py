#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from path import path

# 프로필 노출
def profile_check(드라이버):
    try:
        드라이버.find_element_by_xpath(path.프로필아이콘)

    except Exception as ex:
        print('오류가 발생 하였습니다. 내용을 확인 하세요. > {}'.format(ex))
        
        if 드라이버.find_element_by_xpath('//a[@class="btn_basic btn_primary "]'):
            print('웹에서 로그인 하신 후, 하기 설정 후 재 시도 하십시요.')
            print('[계정관리 > 보안 > 로그인 기기관리]에서 - 모든기기에서 로그인을 허용합니다 - ')

# 프로필 클릭
def profile_click(드라이버):
    드라이버.find_element_by_xpath(path.프로필아이콘).click()

# 글쓰기 클릭
def profile_write(드라이버):
    드라이버.find_element_by_xpath(path.블로그글쓰기).click()

