from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By

desired_capabilities = dict(
    deviceName='Android',
    platformName='Android',
    browserName= 'Chrome',
    automationName='UiAutomator2'

)
capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
driver.get("https://www.google.com/")
driver.find_element(By.XPATH,'//*[@id="tsf"]/div[1]/div[1]/div[1]/div[1]/div/textarea').send_keys("Iphone 15")
