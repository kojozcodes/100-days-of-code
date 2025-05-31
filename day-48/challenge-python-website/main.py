from selenium import webdriver
from selenium.webdriver.common.by import By

python_url = "https://www.python.org/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(python_url)

event_elements = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery .menu li")

upcoming_events = {
    str(i): {
        "time": event.find_element(By.TAG_NAME, "time").get_attribute("datetime").split("T")[0],
        "name": event.find_element(By.TAG_NAME, "a").text
    }
    for i, event in enumerate(event_elements)
}

print(upcoming_events)

driver.quit()
