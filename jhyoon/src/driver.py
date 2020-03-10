#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# 암묵적 명시, 5초 설정 및 해당 함수 호출 시 드라이버 반환

def driver():

    options = Options()
    options.headless = True
    드라이버 = webdriver.Chrome(executable_path="..\chromedriver.exe", options=options)

    return 드라이버

