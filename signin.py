from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, "fName")
l_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

f_name.send_keys("Harold")
l_name.send_keys("Babtock")
email.send_keys("hbab@kbab.gov")

# email.send_keys(Keys.ENTER)
# # OR
# submit = driver.find_element(By.CSS_SELECTOR, "form button")
# submit.click