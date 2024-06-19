import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

desired_capabilities = dict(
    deviceName='Android',
    platformName='Android',
    browserName= 'Chrome',
    automationName='UiAutomator2'

)
capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
driver.get("https://www.wikipedia.org/")
dropdown = driver.find_element(By.CSS_SELECTOR,'#searchLanguage')
select = Select(dropdown)
select.select_by_value("hi")

options = driver.find_element(By.TAG_NAME,'option')

print(len(options))
for option in options:
    print("Text is : ",option.text , "Lang is : ",option.get_attribute('Lang') )
time.sleep(2)
driver.quit()
