from selenium import webdriver
from selenium.webdriver.common.by import By

chromedriver_path = "/Users/excalibur/Desktop/100days_python/chromedriver"

driver = webdriver.Chrome(executable_path=chromedriver_path)

driver.get("https://www.amazon.com/dp/B0797HZ8W1/ref=as_li_ss_tl?SubscriptionId=AKIAJO7E5OLQ67NVPFZA&ascsubtag=880201837-2-1877782055.1660859258&tag=brg_ana_2-20")
#open a new browser window with the specified driver

dollars = driver.find_element(By.CLASS_NAME, "a-price-whole")
cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
print(dollars.text + "." + cents.text)

driver.close()