# -*- coding: utf-8 -*-
#모듈 선언
#selenium :자동화 모듈
#time : 시간 모듈
from selenium import webdriver # c:\>pip install selenium
import pywinauto # c:\>pip install pywinauto
import time

chrome_file = 'c:\\chromedriver.exe' #크롬드라이버 경로
url = 'https://www.tistory.com/' #접속 주소 
account = '계정'#계정
password = '비밀번호' #비밀번호
title = '블로그 제목' #블로그 제목
content = '블로그 내용' #블로그 내용
tag = '블로그 태그' #태그 작성
attr = 'C:\test.png' #업로디용 사진 경로

#윈도우에서 파일 다이얼로그를 컨트롤 할 수 있는 함수 
def upload_img(filepath):
    app = pywinauto.application.Application().connect(title_re="열기")
    app.열기.Edit.set_edit_text(filepath)
    app.열기.Button.click()

#실행 : 웹드라이브 실행 및 진행 스텝
driver = webdriver.Chrome(chrome_file) #웹드라이브 크롬 객체 [경로입력]
driver.implicitly_wait(10) #웹드라이브 대기 10초
driver.get(url) #티스토리 페이지로 이동 [url입력]

#로그인
driver.find_element_by_xpath("//*[@id='kakaoHead']/div/div[3]/div/a[1]").click() #로그인클릭
time.sleep(2) #대기 2초
driver.find_element_by_xpath("//*[@id='loginId']").send_keys(account)#계정입력
time.sleep(2) #대기 2초
driver.find_element_by_xpath("//*[@id='loginPw']").send_keys(password)#비번입력
time.sleep(2) #대기 2초
driver.find_element_by_xpath("//*[@id='authForm']/fieldset/button").click()#로그인 버튼 클릭
time.sleep(2) #대기 2초

#글쓰기 페이지로 이동
driver.find_element_by_xpath("//*[@id='kakaoHead']/div/div[3]/div/a[2]/img").click()#계정정보 클릭
time.sleep(2) #대기 2초
driver.find_element_by_xpath("//*[@id='kakaoHead']/div/div[3]/div/div/div/div[2]/div/div[1]/a[1]").click()#첫번째 블로그 클릭
time.sleep(2) #대기 2초
driver.find_element_by_xpath("//*[@id='footer']/p/a[2]").click()#관리자모드 클릭
time.sleep(2) #대기 2초
driver.find_element_by_xpath("//*[@id='mFeature']/div[2]/a[1]").click()#글쓰기 선택
time.sleep(2) #대기 2초

#글쓰기 진행
driver.find_element_by_xpath("//*[@id='editorContainer']/div[1]/div/button/i[1]").click()#카테고리 목록 펼치기
time.sleep(2) #대기 2초
driver.find_element_by_xpath("//*[@id='editorContainer']/div[1]/div[2]/div/div[2]/span").click() #카테고리 선택
time.sleep(2) #대기 2초
driver.find_element_by_xpath("//*[@id='editorContainer']/div[2]/textarea").send_keys(title) #제목 입력
time.sleep(2) #대기 2초
driver.find_element_by_xpath("//*[@id='tagText']").send_keys(tag)#태그 입력
time.sleep(5) #대기 5초
driver.switch_to_frame(0) #frame 변경
driver.find_element_by_xpath("//*[@id='tinymce']").send_keys(content)#내용 입력
time.sleep(5) #대기 5초
driver.switch_to.default_content() #원래 frame로 변경
time.sleep(2) #대기 2초

#사진 파일 첨부
driver.find_element_by_xpath("//*[@id='mceu_0-open']/i[1]").click()#첨부파일 클릭
time.sleep(2) #대기 2초
driver.find_element_by_xpath("//*[@id='mceu_35-text']").click()#사진 선택
time.sleep(2)
upload_img(attr)#파일 첨부
time.sleep(2) #대기 2초

#옵션 설정 및 저장
driver.find_element_by_xpath("//*[@id='kakaoWrap']/div[3]/div[2]/button").click() #1차 저장
time.sleep(2) #대기 2초
driver.find_element_by_xpath('''//*[@id="open0"]''').click()#비공개 클릭
time.sleep(2) #대기 2초
driver.find_element_by_xpath("//*[@id='editor-root']/div[6]/div/div/div/form/fieldset/div[3]/div/button[2]").click() #최종저장
time.sleep(2) #대기 2초

#종료
driver.close() #웹드라이브 종료