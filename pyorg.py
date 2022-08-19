from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chromedriver_path = "/Users/excalibur/Desktop/100days_python/chromedriver"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.python.org")

