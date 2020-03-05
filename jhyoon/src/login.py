#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import sys
import os
import getpass

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from path import path

# 로그인
def login(드라이버):

    드라이버.get(path.티스토리)

    id = input('id 입력 : ')
    pw = getpass.getpass('pw 입력 : ')

    드라이버.find_element_by_link_text('로그인하기').click()
    드라이버.find_element_by_name('loginId').send_keys(id)
    드라이버.find_element_by_name('password').send_keys(pw)
    드라이버.find_element_by_name('password').send_keys(Keys.ENTER)
