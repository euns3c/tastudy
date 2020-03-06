# -*- coding: utf-8 -*-
#모듈 선언
#selenium :자동화 모듈
#time : 시간 모듈

from selenium import webdriver # c:\>pip install selenium
from bs4 import BeautifulSoup
import pytest
import time

#변수 넣기
tid = '[아이디입력]'
tpw = '[비밀번호입력]'
title = '제목입력'
content = '내요입력'
tag = '태그입력'
result_url =' ' #결과 URL저장하는 곳

@pytest.fixture()
def setup():
#실행 : 웹드라이브 실행 및 진행 스텝
    global driver
    driver = webdriver.Chrome('c:\\chromedriver.exe') 
    print("#웹드라이브 크롬 객체 [경로입력]")
    driver.implicitly_wait(10) 
    print("#웹드라이브 대기 10초")
    yield
    driver.close()

#티스토리에 글을 쓰는 테스트 케이
def test_t_writer(setup):
    global result_url
    driver.get('https://www.tistory.com/') 
    print("#티스토리 페이지로 이동 [url입력]")
          
    #로그인
    driver.find_element_by_xpath("//*[@id='kakaoHead']/div/div[3]/div/a[1]").click() 
    print("#로그인클릭")
    time.sleep(2) #대기 2초
    driver.find_element_by_xpath("//*[@id='loginId']").send_keys(tid)
    print("#계정입력 [계정입력]")
    time.sleep(2) #대기 2초
    driver.find_element_by_xpath("//*[@id='loginPw']").send_keys(tpw)
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
    driver.find_element_by_xpath("//*[@id='editorContainer']/div[2]/textarea").send_keys(title) 
    print("#제목 입력 [블로그 제목입력]")
    time.sleep(2) #대기 2초
    driver.find_element_by_xpath("//*[@id='tagText']").send_keys(tag)
    print("#태그 입력 [태그 입력]")
    time.sleep(5) #대기 5초
    
    iframe = driver.find_element_by_css_selector('.mce-edit-area.mce-container.mce-panel.mce-stack-layout-item.mce-last iframe')
    driver.switch_to.frame(iframe)
    driver.find_element_by_xpath("//*[@id='tinymce']").send_keys(content)
    print("#내용 입력 [블로그 내용입력]")
    time.sleep(5) #대기 5초
    driver.switch_to.default_content() 
    print("#원래 frame로 변경")
    time.sleep(2) #대기 2초    
    
    #옵션 설정 및 저장
    driver.find_element_by_xpath("//*[@id='kakaoWrap']/div[3]/div[2]/button").click() 
    print("#1차 저장")
    time.sleep(2) #대기 2초
    driver.find_element_by_xpath('''//*[@id="open20"]''').click()
    print("#공개 클릭")
    time.sleep(2) #대기 2초
    driver.find_element_by_xpath("//*[@id='editor-root']/div[6]/div/div/div/form/fieldset/div[3]/div/button[2]").click() 
    print("#최종저장")
    time.sleep(2) #대기 2초
    #저장한 페이지 주소를 알아내서 저장한다.
    souppp = BeautifulSoup(driver.page_source, 'html.parser')
    result_url = souppp.findAll('strong',{'class':'tit_post tit_ellip'})[0].find_all('a')[0]['href']
    print(result_url)
    time.sleep(10)
    assert True
    
    #작성된 내용 확인하는 테스트 케이스 
def test_t_check(setup): 
    print(result_url)
    driver.get(result_url)    
    souppp = BeautifulSoup(driver.page_source, 'html.parser')
    assert title == souppp.findAll('meta', {'name':'title'})[0]['content'] #작성한 제목과 실제 작성된 제목을 비교
    assert content == souppp.findAll('meta', {'name':'description'})[0]['content']#작성한 내용과 실제 작성된 내용을 비교 
    assert tag == [i.get_text() for i in souppp.findAll('a', {'rel':'tag'})][0] #작성한 태그랑 작성된 태그 비교
    assert True
    
#reportsms 콘솔에서 생성하게 진행한다.