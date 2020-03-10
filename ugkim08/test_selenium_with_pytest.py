from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
import pytest
from pywinauto import application
import warnings
warnings.simplefilter('ignore', UserWarning)


@pytest.fixture()
def test_setup():
    global driver
    path = 'C:/chromedriver.exe'
    driver = Chrome(path)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get('https://www.tistory.com')
    driver.find_element(By.XPATH, '//*[@id="kakaoHead"]/div/div[3]/div/a[1]').click()
    # email주소 및 pw입력
    driver.find_element(By.NAME, 'loginId').send_keys('Email')
    time.sleep(0.5)
    driver.find_element(By.NAME, 'password').send_keys('PW')
    time.sleep(0.5)
    # 로그인 버튼 클릭
    driver.find_element(By.CLASS_NAME, 'btn_login').click()
    time.sleep(1)
    print('로그인 완료')
    yield
    driver.close()
    driver.quit()
    print("테스트 완료")

def upload_img(filepath):
    app = application.Application().connect(title_re="열기")
    app.열기.Edit.set_edit_text(filepath)
    app.열기.Button.click()

# 티스토리 로그인 케이스
def test_login_tistory(test_setup):
    time.sleep(2)
    # 썸네일 버튼 노출로 로그인 확인
    driver.find_element(By.CLASS_NAME, 'thumb_profile').click()
    time.sleep(0.5)
    private_info = driver.find_element(By.CLASS_NAME, 'inner_header_layer')
    if private_info.is_displayed():
        print('개인정보 레이어 노출 확인 > 로그인 완료')
    else:
        print('개인정보 레이어 미노출 > 테스트 실패')
        driver.quit()
    time.sleep(1)

# 글쓰기 페이지 이동 > 글 작성 케이스
def test_create_article(test_setup):
    time.sleep(1)
    # 썸네일 버튼 선택
    driver.find_element(By.CLASS_NAME, 'thumb_profile').click()
    # 글쓰기 버튼 선택
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="kakaoHead"]/div/div[3]/div/div/div/div[2]/div/div/a[2]').click()
    time.sleep(0.5)
    # 타이틀 입력
    driver.find_element(By.CLASS_NAME, 'textarea_tit').send_keys('제목 입력')
    print('타이틀 입력 완료')
    iframe = driver.find_element(By.CSS_SELECTOR, '.mce-edit-area.mce-container.mce-panel.mce-stack-layout-item.mce-last iframe')
    driver.switch_to.frame(iframe)
    # 본문 내용 입력
    driver.find_element(By.TAG_NAME, 'p').send_keys("본문내용입력.")
    driver.switch_to.default_content()
    print('본문내용 입력 완료')
    # 사진 첨부
    driver.find_element(By.ID, 'mceu_0-open').click()
    time.sleep(1)
    driver.find_element(By.ID, 'mceu_32').click()
    time.sleep(3)
    upload_img(r'C:\Users\UGkim\Desktop\edit_pic\1.jpg')
    time.sleep(5)
    # 태그 추가
    tag_input = driver.find_element(By.ID, 'tagText')
    tag_input.send_keys('테스트')
    tag_input.send_keys(Keys.ENTER)
    time.sleep(2)
    # 완료 버튼 선택
    driver.find_element(By.XPATH, '//*[@id="kakaoWrap"]/div[3]/div[2]/button').click()
    time.sleep(2)
    # 비공개 설정
    private_radio_btn = driver.find_element(By.ID, 'open0')

    if private_radio_btn.is_selected():
        pass
    else:
        private_radio_btn.click()
    time.sleep(2)

    # 비공개 저장 버튼 선택
    driver.find_element(By.XPATH, '//*[@id="editor-root"]/div[6]/div/div/div/form/fieldset/div[3]/div/button[2]').click()
    time.sleep(2)

# 실패 케이스
def test_confirm_aticle(test_setup):
    driver.get('https://zika.tistory.com/manage/posts/')
    time.sleep(1)
    if driver.find_element(By.XPATH, '//*[@id="mArticle"]/div/h3_!').is_displayed():
        pass
    else:
        print("테스트 실패")
        driver.quit()
    time.sleep(1)

