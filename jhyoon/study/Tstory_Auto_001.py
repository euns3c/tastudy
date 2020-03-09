#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import sys
import os
import time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from src import login
from src import driver
from src import main
from src import write_page
from path import path

드라이버 = driver.driver()
드라이버.implicitly_wait(5)

# 로그인
login.login(드라이버)

# 프로필 노출 확인
main.profile_check(드라이버)

# 프로필 클릭
main.profile_click(드라이버)

# 글쓰기 클릭
main.profile_write(드라이버)

# 카테고리 노출 확인
write_page.category_view(드라이버)

# 제목 노출 확인
write_page.title_view(드라이버)

# 제목 입력
내용 = '제목 입니다. 작성 시간은 {}'.format(time.strftime("%H:%M:%S", time.localtime(time.time())))
write_page.title_write(드라이버, 내용)

# 내용 입력
내용 = '가나다라마바사'
write_page.body_write(드라이버, 내용)

# 원래의 프레임으로 전환
드라이버.switch_to.default_content()

# 태그 입력
내용 = '하나'
write_page.tag_write(드라이버, 내용)

# 저장
드라이버.find_element_by_xpath(path.완료).click()

# 비공개저장 클릭
드라이버.find_element_by_xpath(path.비공개저장).click()

time.sleep(3)

# 종료
드라이버.quit()


