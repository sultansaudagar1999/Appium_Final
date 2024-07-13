import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By

desired_capabilities = dict(
    deviceName='Android',
    platformName='Android',
    appPackage='com.android.chrome',
    appActivity='org.chromium.chrome.browser.ChromeTabbedActivity',
    automationName='UiAutomator2'

)
capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)


driver.get("https://www.google.co.in/")
time.sleep(2)

webview = driver.contexts[1]
driver.switch_to.context(webview)

driver.find_element(By.XPATH,'//android.widget.EditText').send_keys("Hello Appium !!!!")


driver.quit()

