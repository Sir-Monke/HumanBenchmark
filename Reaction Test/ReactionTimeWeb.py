from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://humanbenchmark.com/login")
driver.implicitly_wait(0.5)

click = True
end_of_game = 5
total_clicks = 0

usernameInputBox = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/div/form/p[1]/input').send_keys("USERNAME")
passwordInputBox = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/div/form/p[2]/input').send_keys("PASS")
loginBtn = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/div/form/p[3]/input').click()

driver.get("https://humanbenchmark.com/tests/reactiontime")
time.sleep(2)
driver.refresh()
reactionTimeButton = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]')

while True:
    if total_clicks != end_of_game:
        if "view-go e18o0sx0 css-saet2v e19owgy77" in reactionTimeButton.get_attribute("class"):
            if click:
                reactionTimeButton.click()
                click = False
        if "view-result e18o0sx0 css-saet2v e19owgy77" or "view-splash e18o0sx0 css-saet2v e19owgy77" in reactionTimeButton.get_attribute("class"):
            if not click:
                reactionTimeButton.click()
                click = True
                total_clicks += 1
    else:
        saveScoreBtn = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div[3]/button[1]')
        saveScoreBtn.click()
        time.sleep(10)
driver.quit()

