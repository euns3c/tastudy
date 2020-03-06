# -*- coding: utf-8 -*-
#모듈 선언
#selenium :자동화 모듈
#time : 시간 모듈
from selenium import webdriver # c:\>pip install selenium
import pywinauto # c:\>pip install pywinauto
import time
from bs4 import BeautifulSoup
import re

#윈도우에서 파일 다이얼로그를 컨트롤 할 수 있는 함수 
def upload_img(filepath):
    app = pywinauto.application.Application().connect(title_re="열기")
    app.열기.Edit.set_edit_text(filepath)
    app.열기.Button.click()

#실행 : 웹드라이브 실행 및 진행 스텝
driver = webdriver.Chrome('c:\\qa\\chromedriver.exe') 
print("#웹드라이브 크롬 객체 [경로입력]")
driver.implicitly_wait(10) 
print("#웹드라이브 대기 10초")
driver.get('https://www.tistory.com/') 
print("#티스토리 페이지로 이동 [url입력]")


#로그인
driver.find_element_by_xpath("//*[@id='kakaoHead']/div/div[3]/div/a[1]").click() 
print("#로그인클릭")
time.sleep(2) #대기 2초
driver.find_element_by_xpath("//*[@id='loginId']").send_keys('계정입력')
print("#계정입력 [계정입력]")
time.sleep(2) #대기 2초
driver.find_element_by_xpath("//*[@id='loginPw']").send_keys('비번입력')
print("#비번입력 [비밀번호]")
time.sleep(2) #대기 2초
driver.find_element_by_xpath("//*[@id='authForm']/fieldset/button").click()
print("#로그인 버튼 클릭")
time.sleep(2) #대기 2초

#글쓰기 페이지로 이동
driver.find_element_by_xpath("//*[@id='kakaoHead']/div/div[3]/div/a[2]/img").click()
print("#계정정보 클릭")
time.sleep(2) #대기 2초
driver.find_element_by_xpath("//*[@id='kakaoHead']/div/div[3]/div/div/div/div[2]/div/div[1]/a[1]").click()
print("#첫번째 블로그 클릭")
time.sleep(2) #대기 2초
driver.find_element_by_xpath("//*[@id='footer']/p/a[2]").click()
print("#관리자모드 클릭")
time.sleep(2) #대기 2초
driver.find_element_by_xpath("//*[@id='mFeature']/div[2]/a[1]").click()
print("#글쓰기 선택")
time.sleep(2) #대기 2초

#글쓰기 진행
driver.find_element_by_xpath("//*[@id='editorContainer']/div[1]/div/button/i[1]").click()
print("#카테고리 목록 펼치기")
time.sleep(2) #대기 2초
driver.find_element_by_xpath("//*[@id='editorContainer']/div[1]/div[2]/div/div[2]/span").click() 
print("#카테고리 선택")
time.sleep(2) #대기 2초
driver.find_element_by_xpath("//*[@id='editorContainer']/div[2]/textarea").send_keys('테스트용 제목입력입니다.') 
print("#제목 입력 [블로그 제목입력]")
time.sleep(2) #대기 2초
driver.find_element_by_xpath("//*[@id='tagText']").send_keys('테스트용태그')
print("#태그 입력 [태그 입력]")
time.sleep(5) #대기 5초
driver.switch_to_frame(0) #frame 변경
driver.find_element_by_xpath("//*[@id='tinymce']").send_keys('안녕하세요 티스토리 블로그 테스트 자동화 입력입니다. \n 반갑습니다.')
print("#내용 입력 [블로그 내용입력]")
time.sleep(5) #대기 5초
driver.switch_to.default_content() 
print("#원래 frame로 변경")
time.sleep(2) #대기 2초

#사진 파일 첨부
driver.find_element_by_xpath("//*[@id='mceu_0-open']/i[1]").click()
print("#첨부파일 클릭")
time.sleep(2) #대기 2초
driver.find_element_by_xpath("//*[@id='mceu_35-text']").click()
print("#사진 선택")
time.sleep(2)
upload_img(r'd:\all.png')
print("#파일 첨부 [사진 파일 경로 입력]")
time.sleep(2) #대기 2초
soup = BeautifulSoup(driver.page_source, 'html.parser')
up_btn = soup.findAll('div',{'class':'mce-widget mce-btn mce-primary mce-flow-layout-item mce-last mce-btn-has-text'})
btn_id = re.findall('mceu_[0-9]+-button', str(up_btn))[0]
print("#첨부사진 확인버튼 찾기 완료")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='"+btn_id+"']/span").click() 
print("#첨부사진 확인버튼 클릭")

#옵션 설정 및 저장
driver.find_element_by_xpath("//*[@id='kakaoWrap']/div[3]/div[2]/button").click() 
print("#1차 저장")
time.sleep(2) #대기 2초
driver.find_element_by_xpath('''//*[@id="open0"]''').click()
print("#비공개 클릭")
time.sleep(2) #대기 2초
driver.find_element_by_xpath("//*[@id='editor-root']/div[6]/div/div/div/form/fieldset/div[3]/div/button[2]").click() 
print("#최종저장")
time.sleep(2) #대기 2초

#종료
driver.close() 
print("#웹드라이브 종료")