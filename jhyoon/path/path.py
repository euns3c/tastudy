#-*- coding:utf-8 -*-
# 주소
티스토리 = 'https://www.tistory.com/'

# 메인페이지
프로필아이콘 = '//a[@class="link_profile"]'
운영중블로그 = '//a[@class="txt_id"]'
블로그글쓰기 = '//a[@class="img_common_tistory link_edit"]'

# 블로그페이지
글쓰기 = '//a[@class="write"]'

# 글쓰기페이지
카테고리_셀렉트 = '//i[@class="mce-txt" and text()="카테고리"]'
제목_인풋 = '//textarea[@class="textarea_tit"]'
# placeholder = '제목을 입력하세요'
# 입력값은 text 문자열로 저장됨
내용_텍스트박스 = '//body[@class="mce-content-body content"]/p'
#내용_입력확인 = '{}'.format(내용_텍스트박스) + '/p'
태그 = '//input[@type="text"]'
완료 = '//button[@type="button" and @class="btn btn-default"]'
비공개저장 = '//div[@class="wrap_btn"]//button[@class="btn btn-default" and @type="submit"]'