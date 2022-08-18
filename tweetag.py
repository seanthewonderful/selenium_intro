from selenium import webdriver
from selenium.webdriver.common.by import By

chromedriver_path = "/Users/excalibur/Desktop/100days_python/chromedriver"

driver = webdriver.Chrome(executable_path=chromedriver_path)

ht1 = "sponsored"
ht2 = "golf"

# driver.get(f"https://mobile.twitter.com/hashtag/{hashtag}?f=live")

driver.get(f"https://mobile.twitter.com/search?q=%23{ht1}%20%23{ht2}&src=typed_query&f=live")

# tweets = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span[1]')

tweets = driver.find_elements(By.TAG_NAME, "span")

for tweet in tweets:
    print(tweet.text)

# print(tweets)

driver.close()