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
            
        # print(shop_dict)

        for k, v in shop_dict.items():
            money = int(driver.find_element(By.ID, "money").text.split(" ")[-1].replace(",",""))

            if money > k:
                buy = driver.find_element(By.ID, v)
                buy.click()
                k = int(driver.find_element(By.CSS_SELECTOR, f"#{v} b").text.split(" ")[-1].replace(",", ""))
                
                # while money > k:
                #     print("$: ", money)
                #     print("K: ", k)
                #     driver.find_element(By.ID, v).click()
                #     money = int(driver.find_element(By.ID, "money").text.split(" ")[-1].replace(",",""))
                #     k = int(driver.find_element(By.CSS_SELECTOR, f"#{v} b").text.split(" ")[-1].replace(",", ""))

        five_secs = time.time() + 5
    
    if time.time() > five_mins:
        cooks_ps = driver.find_element(By.ID, "cps")
        cps = cooks_ps.split(" ")[-1].replace(",", "")
        print(f"Cookies Per Second: {cps}")
        break
        
    
# while time.time() < five_mins:
#     if money < cursor_price:
#         pass
#     while time.time() < five_secs:
#         cookie.click()
        
#     while money > 123456789:
#         time_machine.click()
        
#     while money > 1000000:
#         portal.click()
        
#     while money > 50000:
#         alchemy_lab.click()
        
#     while money > 7000:
#         shipment.click()
        
#     while money > 2000:
#         mine.click()
        
#     while money > 500:
#         factory.click()
        
#     while money > 500:
#         grandma.click()
        
#     while money > 100:
#         cursor.click()
    
#     continue








# time_machine = driver.find_element(By.ID, "buyTime machine")
# time_machine_price = driver.find_element(By.CSS_SELECTOR, "#buyTime machine b").text.split(" ")[-1].replace(",", "")

# portal = driver.find_element(By.ID, "buyPortal")
# portal_price = driver.find_element(By.CSS_SELECTOR, "#buyPortal b").text.split(" ")[-1].replace(",", "")

# alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab")
# # alchemy_lab_price = driver.find_element(By.CSS_SELECTOR, "#buyAlchemy lab b").text.split(" ")[-1].replace(",", "")

# shipment = driver.find_element(By.ID, "buyShipment")
# shipment_price = driver.find_element(By.CSS_SELECTOR, "#buyShipment b").text.split(" ")[-1].replace(",", "")

# mine = driver.find_element(By.ID, "buyMine")
# mine_price = driver.find_element(By.CSS_SELECTOR, "#buyMine b").text.split(" ")[-1].replace(",", "")

# factory = driver.find_element(By.ID, "buyFactory")
# factory_price = driver.find_element(By.CSS_SELECTOR, "#buyFactory b").text.split(" ")[-1].replace(",", "")

# grandma = driver.find_element(By.ID, "buyGrandma")
# grandma_price = driver.find_element(By.CSS_SELECTOR, "#buyGrandma b").text.split(" ")[-1].replace(",", "")

# cursor = driver.find_element(By.ID, "buyCursor")
# cursor_price = driver.find_element(By.CSS_SELECTOR, "#buyCursor b").text.split(" ")[-1]