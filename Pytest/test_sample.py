import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Test.Scrollutility import ScrollUtil

desired_capabilities = dict(
    deviceName='Android',
    platformName='Android',
    app='C:\\Users\\DefineLabs-PC\\PycharmProjects\\VCS-Control-Project\\Apk\\Goibibo.apk',
    automationName='UiAutomator2'

)
capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
driver.implicitly_wait(10)

driver.find_element(By.ID,'com.goibibo:id/onboarding_enter_mob_no_edtTxt').send_keys("9762628372")
driver.find_element(By.ID,'com.goibibo:id/onboarding_continue_cardVw').click()
time.sleep(10)
