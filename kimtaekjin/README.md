# 티스토리 블로그 작성 자동화

1차 테스트 자동화 스터디 주제는 티스토리 블로그 작성입니다.

## 목적

웹사이트 테스트 시 자동으로 글을 작성하는 테스트를 자동으로 해주는 목적으로 진행한다.

## 진행 스텝

01. 티스토리 접속
02. 로그인
03. 블로그 이동
04. 블로그 작성 페이지로 이동
05. 글작성 - 카테고리 선택
06. 글작성 - 제목 입력
07. 글작성 - 태그 입력
08. 글작성 - 내용 입력
09. 글작성 - 사진 선택, 첨부
10. 1차 저장
11. 글 공개 여부 선택
12. 최종 글 저장

## 파일 구성

Tistory_Auto_First.py

: selenium, pywinauto 모듈을 사용하여 티스토리 블로그를 자동으로 제어하였다.

: selenium의 'find_element_by_xpath'를 사용하여 버튼 및 텍스트 박스를 찾았다.

: 단일 자동 수행용으로 작성되었다.


## 사전 준비 사항(파일 다운로드 및 모듈 설치

### 웹드라이버 다운르도
: chromedriver.exe 파일을 검색하여 다운로드를 한다.

### selenium 모듈

pip를 이용하여 다운로드

: pip install selenium
: pip install pywinauto


## 사용법

파일 내 수정사항 

- 16번줄 : driver = webdriver.Chrome('c:\\chromedriver.exe') #웹드라이브 크롬 객체 [경로입력]

    : 크롬드라이버 경로를 본인에 맞게 변경

- 23번줄 : driver.find_element_by_xpath("//*[@id='loginId']").send_keys('계정')#계정입력 [계정입력]

    : 본인의 계정 입력

- 25번줄 : driver.find_element_by_xpath("//*[@id='loginPw']").send_keys('비밀')#비번입력 [비밀번호]

    : 본인의 비밀번호 입력

- 60번줄 : upload_img(r'C:\test.png')#파일 첨부 [사진 파일 경로 입력]

    : 사진 파일의 경로 입력

### 폴더 구조

other code
 - Tistory_Auto_Second.py
 
    : 변수로 입력 사항을 따로 뽑은 파일
 
 - Tistory_Auto_First.py
 
    : 모든 입력 사항을 따로 리스트로 저장해 사용한 파일