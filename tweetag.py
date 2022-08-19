from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chromedriver_path = "/Users/excalibur/Desktop/100days_python/chromedriver"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

ht1 = "sponsored"
ht2 = "golf"

# driver.get(f"https://mobile.twitter.com/hashtag/{hashtag}?f=live")

driver.get(f"https://mobile.twitter.com/search?q=%23{ht1}%20%23{ht2}&src=typed_query&f=live")

# tweets = driver.find_element(By.CLASS_NAME, 'r-qvutc0')

tweets = driver.find_elements(By.CSS_SELECTOR, "span .css-901oao")

# for tweet in tweets:
#     print(tweet)

# print(tweets.get_attribute("class"))
print(tweets)
driver.close()