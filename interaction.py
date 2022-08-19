from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chromedriver_path = "/Users/excalibur/Desktop/100days_python/chromedriver"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://en.wikipedia.org/wiki/Main_Page")

""" Clicking and sending keys """
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

# wikiversity = driver.find_element(By.LINK_TEXT, "Wikiversity")
# wikiversity.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# print(article_count.text)

# driver.quit()