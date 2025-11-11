import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
url = "https://map.naver.com/p/entry/place/2012416294"
driver.get(url)
driver.implicitly_wait(10)

# 명시적 대기 객체 생성
wait = WebDriverWait(driver, 10)

# iframe으로 전환 (iframe의 ID로 접근)
wait.until(EC.frame_to_be_available_and_switch_to_it("entryIframe"))

# 예약 클릭하기
# driver.find_elements(By.CLASS_NAME,"yxkiA")[-1].click()
reservation_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='yxkiA'][./a/span[text()='예약']]")))
reservation_button.click()

# 예약 상세페이지 들어가기
# driver.find_elements(By.CLASS_NAME,"P2Qvt")[-1].click()
detail_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='P2Qvt']")))
detail_button.click()

# 날짜 클릭하기 (11월 17일)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "calendar_date")))
date_elements = driver.find_elements(By.CLASS_NAME, "calendar_date")
try:
    for date_element in date_elements:
        if date_element.find_element(By.CLASS_NAME,"num").text == "17":
            date_element.click()
            break
except Exception as e:
    print("❗ 오류 발생:", e)

# 시간 클릭하기 (오후 6시)
# driver.find_elements(By.CLASS_NAME,"btn_time")[-1].click()
time_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn_time' and text()='6:00']")))
time_button.click()

# 다음 클릭하기
# driver.find_element(By.CLASS_NAME,"NextButton__btn_next__kfLFW").click()
next_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"NextButton__btn_next__kfLFW")))
next_button.click()

