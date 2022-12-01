from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://SunInJuly.github.io/execute_script.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)

    num = browser.find_element(By.ID, "input_value")
    x = num.text
    y = calc(x)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()
    radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio.click()
    button.click()

finally:
    time.sleep(10)
    browser.quit()
