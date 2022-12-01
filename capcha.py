from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    textarea = browser.find_element(By.ID, "answer")
    textarea.send_keys(y)
    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()
    radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
