from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pywinauto import application
import warnings # UserWarning: 64-bit application should be automated using 64-bit Python (you use 32-bit Python) 해결방법
warnings.simplefilter('ignore', category=UserWarning) # UserWarning: 64-bit application should be automated using 64-bit Python (you use 32-bit Python) 해결방법

path = ('C:/chromedriver.exe')
driver = webdriver.Chrome(path)
url = 'https://www.tistory.com/'

time.sleep(1)

def upload_img(filepath):
    app = application.Application().connect(title_re="열기")
    app.열기.Edit.set_edit_text(filepath)
    app.열기.Button.click()

# 티스토리 접속
driver.get(url)

# 브라우저 크기를 1260 x 890으로 조정
driver.set_window_size(1280, 950)

time.sleep(0.5)

# 티스토리 메인 > 로그인 페이지 이동
driver.find_element(By.XPATH, '//*[@id="kakaoHead"]/div/div[3]/div/a[1]').click()

# email주소 및 pw입력
driver.find_element(By.NAME, 'loginId').send_keys('Email')
time.sleep(0.5)
driver.find_element(By.NAME, 'password').send_keys('PW')
time.sleep(0.5)

# 로그인 버튼 클릭
driver.find_element(By.CLASS_NAME, 'btn_login').click()
time.sleep(1)

# 썸네일 아이콘을 통해 글쓰기 페이지 진입
driver.find_element(By.CLASS_NAME, 'thumb_profile').click()
time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="kakaoHead"]/div/div[3]/div/div/div/div[2]/div/div/a[2]').click()
time.sleep(1)

# 타이틀 작성

time.sleep(1)
driver.find_element(By.CLASS_NAME, 'textarea_tit').send_keys('타이틀 입력')

# 본문 내용 작성
iframe = driver.find_element(By.CSS_SELECTOR, '.mce-edit-area.mce-container.mce-panel.mce-stack-layout-item.mce-last iframe')
driver.switch_to.frame(iframe)
driver.find_element(By.TAG_NAME, 'p').send_keys("본문내용입력.")
# 기존 프레임으로 이동
driver.switch_to.default_content()

# 사진 첨부
driver.find_element(By.ID, 'mceu_0-open').click()
time.sleep(1)
driver.find_element(By.ID, 'mceu_32').click()
time.sleep(1)
upload_img(r'C:\Users\UGkim\Desktop\1.jpg')
time.sleep(5)

# 태그 달기
tag_input = driver.find_element(By.ID, 'tagText')
tag_input.send_keys('테스트')
tag_input.send_keys(Keys.ENTER) # selenium으로 엔터키 입력 참고 (https://l0o02.github.io/2018/06/12/python-crawling-selenium-2/)
time.sleep(2)

# 완료 버튼 선택
driver.find_element(By.XPATH, '//*[@id="kakaoWrap"]/div[3]/div[2]/button').click()
time.sleep(2)

# 비공개 설정
open_radio_btn = driver.find_element(By.ID, 'open15')
private_radio_btn = driver.find_element(By.ID, 'open0')

if private_radio_btn.is_selected():
    pass
else:
    private_radio_btn.click()
time.sleep(2)

# 비공개 저장 버튼 선택
driver.find_element(By.XPATH, '//*[@id="editor-root"]/div[6]/div/div/div/form/fieldset/div[3]/div/button[2]').click()
time.sleep(2)

# 글작성 완료 > 글관리 페이지 진입 확인

if driver.find_element(By.XPATH, '//*[@id="mArticle"]/div/h3').is_displayed():
    pass
else:
    print("테스트 실패")
    driver.quit()

time.sleep(2)
