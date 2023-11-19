from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 0.2)

click = True
total_clicks = 31
current_clicks = 0

#Login
driver.get("https://humanbenchmark.com/login")
driver.implicitly_wait(0.5)
usernameInputBox = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/div/form/p[1]/input').send_keys("USERNAME")
passwordInputBox = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/div/form/p[2]/input').send_keys("PASS")
loginBtn = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/div/form/p[3]/input').click()

#change to target url
driver.get("https://humanbenchmark.com/tests/aim")
time.sleep(2)
driver.refresh()
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]'))).click()
time.sleep(3)
driver.refresh()

while True:
    if current_clicks != total_clicks:
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div/div/div/div[6]"))).click()
        current_clicks += 1
    else:
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div/div[3]/button[1]'))).click()
        time.sleep(1)
        driver.get("https://humanbenchmark.com/tests/aim")
        driver.refresh()
        time.sleep(1.5)
        current_clicks = 0

driver.quit()
