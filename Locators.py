import time
from threading import Thread

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\marya\\Documents\\Driver2\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH, "//input[@class ='form-control']").send_keys("Maryam")
driver.find_element(By.NAME, "email").send_keys("deemaria02@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.XPATH, "//input[@id='inlineRadio1']")
time.sleep(5)

driver.find_element(By.CSS_SELECTOR, "input[value = 'Submit']").click()
msg = driver.find_element(By.CLASS_NAME, "alert-success").text
print(msg)
assert "Success" in msg