# 티스토리 블로그 api를 통한 글작성 및 검수

3차 스터디 주제 티스토리 api를 이용한 글작성 및 검수

## 목적

api를 이용하고 Pytest를 적용하여 테스트를 진행한다.

## 진행 스텝

01. 티스토리 api로 글 등록을 진행한다.
02. api를 이용한 글 내용을 검증한다.
03. 리포트를 뽑는다.
04. 리포트를 확인한다.

## 파일 구성

Tistory_api_Pytest_finish.py

: requests, Pytest 모듈을 사용한다.


## 사전 준비 사항(파일 다운로드 및 모듈 설치

### 웹드라이버 다운르도
: pip install pytest
: pip install pytest-html
: pip install requests

## 사용법

Tistory_api_Pytest_finish.py파일 실행시 아래와 같이 진행한다.

    : c:/> pytest Tistory_api_Pytest_finish.py --html=report.html