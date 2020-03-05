#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from path import path

# 카테고리 항목 노출
def category_view(드라이버):
    드라이버.find_element_by_xpath(path.카테고리_셀렉트)

# 제목 인풋박스 노출
def title_view(드라이버):
    드라이버.find_element_by_xpath(path.제목_인풋)

# 제목 인풋박스 쓰기
def title_write(드라이버, 내용):
    드라이버.find_element_by_xpath(path.제목_인풋).send_keys('{}'.format(내용))

# 내용 텍스트박스 노출
def body_view(드라이버):
    드라이버.find_element_by_xpath(path.내용_텍스트박스)

# 내용 텍스트박스 쓰기
def body_write(드라이버, 내용):
    드라이버.find_element_by_xpath(path.내용_텍스트박스).click()
    드라이버.find_element_by_xpath(path.내용_텍스트박스).send_keys('{}'.format(내용))

# 태그 노출
def tag_view(드라이버):
    드라이버.find_element_by_xpath(path.태그)

# 태그 쓰기
def tag_write(드라이버, 내용):
    드라이버.find_element_by_xpath(path.태그).clic()
    드라이버.find_element_by_xpath(path.태그).send_keys('{}'.format(내용))
    드라이버.find_element_by_xpath(path.태그).send_keys(Keys.ENTER)