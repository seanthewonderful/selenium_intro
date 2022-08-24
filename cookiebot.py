from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

chromedriver_path = "/Users/excalibur/Desktop/100days_python/chromedriver"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute('id') for item in items]

five_mins = time.time() + 60*5
five_secs = time.time() + 5

while True:
    cookie.click()
    
    if time.time() > five_secs:
        shop_dict = {}
        prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        
        for i in range(len(prices) - 2, -1, -1):
            shop_dict[int((prices[i]).text.split(" ")[-1].replace(",", ""))] = item_ids[i]
            
        print(shop_dict)

        for k, v in shop_dict.items():
            money = int(driver.find_element(By.ID, "money").text.split(" ")[-1].replace(",",""))
            buy = driver.find_element(By.CSS_SELECTOR, f"[id='{v}']")
            print(v)

            if money > k:
                buy.click()

        five_secs = time.time() + 5
    
    if time.time() > five_mins:
        cooks_ps = driver.find_element(By.ID, "cps")
        cps = cooks_ps.split(" ")[-1].replace(",", "")
        print(f"Cookies Per Second: {cps}")
        break
        


                # k = int(driver.find_element(By.CSS_SELECTOR, f"#{v} b").text.split(" ")[-1].replace(",", ""))
                
                # while money > k:
                #     print("$: ", money)
                #     print("K: ", k)
                #     driver.find_element(By.ID, v).click()
                #     money = int(driver.find_element(By.ID, "money").text.split(" ")[-1].replace(",",""))
                #     k = int(driver.find_element(By.CSS_SELECTOR, f"#{v} b").text.split(" ")[-1].replace(",", ""))