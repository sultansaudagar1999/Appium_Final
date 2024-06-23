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
    app='C:\\Users\\DefineLabs-PC\\PycharmProjects\\VCS-Control-Project\\Apk\\Flipboard.apk',
    automationName='UiAutomator2',
    appActivity='flipboard.activities.LaunchActivityAlias',
    appPackage='flipboard.app'
)
capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
driver.implicitly_wait(10)

driver.find_element(By.ID,'flipboard.app:id/first_launch_get_started_button').click()

driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="flipboard.app:id/topic_picker_topic_row_topic_tag" and @text="# UK NEWS"]').click()
driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="flipboard.app:id/topic_picker_topic_row_topic_tag" and @text="# TECHNOLOGY (UK)"]').click()
driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="flipboard.app:id/topic_picker_topic_row_topic_tag" and @text="# SPORTS (UK)"]').click()

driver.find_element(By.ID,'flipboard.app:id/topic_picker_continue_button').click()
driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="flipboard.app:id/icon_button_text" and @text="Skip for Now"]').click()

ScrollUtil.swipeUp(5,driver)
ScrollUtil.swipeLeft(5,driver)
ScrollUtil.swipeRight(5,driver)


time.sleep(3)








driver.quit()