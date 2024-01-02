# 필요한 라이브러리 import =====================
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# ==============================================

# 브라우저 열기
browser = webdriver.Chrome()

page = "원하는 유튜브 커뮤니티 페이지 주소 입력"

# 사이트 접속하기
browser.get(page)
# 로딩 시간을 위한 1초 시간 지연
time.sleep(1)

# ---------- 페이지를 내려야할 경우 --------------------
# 'body' 부분 찾아서 body 변수에 저장
body = browser.find_element(By.CSS_SELECTOR, 'body')

# 원하는 만큼 for문의 숫자를 변경하시면 됩니다.
for i in range(10):
    # 페이지 아래로 내리기
    body.send_keys(Keys.PAGE_DOWN)

# 로딩 시간을 위한 3초 시간 지연
time.sleep(3)
# ----------------------------------------------------

# content-text 라는 id를 가진 것들 가져오기    
datas = browser.find_elements(By.ID, "content-text")

# 데이터 추출
for data in datas:
	print(data.text)

# 1초 시간 지연
time.sleep(1)

# 브라우저 닫기
browser.close()