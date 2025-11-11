import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://map.naver.com/p/entry/place/2012416294")
time.sleep(2)

# iframe의 ID로 접근
driver.switch_to.frame("entryIframe")

# 예약 클릭
driver.find_elements(By.CLASS_NAME,"yxkiA")[-1].click()
time.sleep(2)

# 예약 상세페이지 들어가기
driver.find_elements(By.CLASS_NAME,"P2Qvt")[-1].click()
time.sleep(2)

# 날짜 지정해서 클릭하기 (11월 17일)
date_elements = driver.find_elements(By.CLASS_NAME, "calendar_date")
try:
    for date_element in date_elements:
        if date_element.find_element(By.CLASS_NAME,"num").text == "17":
            date_element.click()
            time.sleep(3)
            break
except Exception as e:
    print("❗ 오류 발생:", e)

# 시간 클릭하기 (오후 6시)
driver.find_elements(By.CLASS_NAME,"btn_time")[-1].click()
time.sleep(2)

# 다음 버튼 클릭하기
driver.find_element(By.CLASS_NAME,"NextButton__btn_next__kfLFW").click()
time.sleep(2)


