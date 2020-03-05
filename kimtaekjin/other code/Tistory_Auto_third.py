# -*- coding: utf-8 -*-
#모듈 선언
#selenium :자동화 모듈
#time : 시간 모듈
from selenium import webdriver # c:\>pip install selenium
import pywinauto # c:\>pip install pywinauto
import time

#로그인 리스트로 구성요소 작성[행동,xpath, 입력값 있으면 넣고, 없으면 쓰지 않음] - 진행 스텝
step = [
['로그인버튼 클릭', "//*[@id='kakaoHead']/div/div[3]/div/a[1]"],
['계정 입력', "//*[@id='loginId']", "[계정을 입력하세요]"],
['비밀번호 입력', "//*[@id='loginPw']", "[비밀번호를 입력하세요]"],
['로그인버튼 클릭', "//*[@id='authForm']/fieldset/button"],
['계정정보버튼 클릭', "//*[@id='kakaoHead']/div/div[3]/div/a[2]/img"],
['블로그버튼 클릭', "//*[@id='kakaoHead']/div/div[3]/div/div/div/div[2]/div/div[1]/a[1]"],
['관리자버튼 클릭', "//*[@id='footer']/p/a[2]"],
['글쓰기버튼 클릭', "//*[@id='mFeature']/div[2]/a[1]"],
['카테고리선택 클릭',"//*[@id='editorContainer']/div[1]/div/button/i[1]"],
['카테고리 드롭박스 선택 클릭',"//*[@id='editorContainer']/div[1]/div[2]/div/div[2]/span"],
['제목 입력',"//*[@id='editorContainer']/div[2]/textarea", "반갑습니다."],
['태그 입력',"//*[@id='tagText']", "welcome!!"],
['글내용 입력',"//*[@id='tinymce']", "환영합니다.\n반갑습니다\n고마워"],
['첨부파일 클릭',"//*[@id='mceu_0-open']/i[1]"],
['사진 클릭',"//*[@id='mceu_35-text']"],
['사진 파일 선택 다이얼로그','C:\test.png', '없음', '없음'],
['1차 저장버튼 클릭',"//*[@id='kakaoWrap']/div[3]/div[2]/button"],
['최종 저장버튼 클릭',"//*[@id='editor-root']/div[6]/div/div/div/form/fieldset/div[3]/div/button[2]"]
]

#실행 : 웹드라이브 실행 및 진행 스텝
driver = webdriver.Chrome('c:\chromedriver.exe') #웹드라이브 크롬 객체 [경로입력]
driver.implicitly_wait(10) #웹드라이브 대기 10초
driver.get('https://www.tistory.com/') #티스토리 페이지로 이동 [url입력]

#윈도우에서 파일 다이얼로그를 컨트롤 할 수 있는 함수 
def upload_img(filepath):
    app = pywinauto.application.Application().connect(title_re="열기")
    app.열기.Edit.set_edit_text(filepath) #[파일 경로 및 파일명 입력]
    app.열기.Button.click()

#driver.find_element_by_xpath 함수
def finder(x):
    global driver
    try: 
        if len(x) == 2: #일반적인 클릭 시 진행
            driver.find_element_by_xpath(x[1]).click()
        elif len(x) == 3: #글 내용 입력 시 진행
            if x[0] =='글내용 입력':
                driver.switch_to_frame(0)
                driver.find_element_by_xpath(x[1]).send_keys(x[2])                
                driver.switch_to.default_content()
            else:
                driver.find_element_by_xpath(x[1]).send_keys(x[2])   
        elif len(x) == 4: #파일 업로드 시 진행
            upload_img(x[1]) #파일업로드 함수 실행
            time.sleep(4)
        time.sleep(3)
        print(x[0] + "진행 완료!")
    
    except Exception as e:
        print("에러발생!")
        print(e)

#블로그 글쓰기 실행
[finder(i) for i in step]

#종료
driver.close()