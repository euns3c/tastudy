from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import pytest

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

# 제목 확인 케이스
def test_confirm_post_title(test_setup):
    time.sleep(0.5)
    # api로 작성한 게시글로 이동
    driver.get('https://zika.tistory.com/11')
    time.sleep(0.5)
    post_title = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/h1').text
    assert post_title == 'api테스트0311'
    time.sleep(0.5)
    print('제목 확인 완료')

# 본문 확인 케이스
def test_confirm_post_content(test_setup):
    time.sleep(0.5)
    driver.get('https://zika.tistory.com/11')
    time.sleep(0.5)
    # 본문 확인
    # post_content로 선언한 xpath값에 온갖 text들이 섞여있어서 post_content에 있는 모든 텍스트를 list로 만들고 해당 리스트에 작성한 값이 있으면 pass하는걸루.....
    content_text = []
    post_content = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]').text
    content_text.append(post_content)
    for i in content_text:
        if 'testcontent' in i:
            print('작성한 텍스트 있음')
            pass
    time.sleep(0.5)
    print('본문 확인 완료')

# 태그 확인 케이스
def test_confirm_post_tag(test_setup):
    time.sleep(0.5)
    driver.get('https://zika.tistory.com/11')
    time.sleep(0.5)
    # 태그 확인
    post_tag = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[3]/div/a').text
    assert post_tag == 'test'
    time.sleep(0.5)
    print('태그 확인 완료')

# pytest -v -s --html=.\report\report0312.html --self-contained-html test_confirm_post.py