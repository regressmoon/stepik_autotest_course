from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/wait1.html"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    button = browser.find_element(By.ID, "verify")
    button.click()

    text_element = browser.find_element(By.ID, "verify_message")
    text = text_element.text
    assert text == "Verification was successful!"

finally:
    time.sleep(10)
    browser.quit()