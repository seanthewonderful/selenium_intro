from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chromedriver_path = "/Users/excalibur/Desktop/100days_python/chromedriver"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.python.org")

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

# for time in event_times:
#     print(time.text)

# for name in event_names:
#     print(name.text)

print(events)

driver.quit()