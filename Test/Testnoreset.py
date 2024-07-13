import time
from hashlib import new

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_capabilities = dict(
    deviceName='Android',
    platformName='Android',
    app='C:\\Users\\DefineLabs-PC\\PycharmProjects\\VCS-Control-Project\\Apk\\Facebooklite.apk',
    automationName='UiAutomator2',
    appActivity='com.facebook.lite.MainActivity',
    appPackage='com.facebook.lite',
    noReset=True

)
capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
driver.implicitly_wait(5)

# email = driver.find_element(By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup')
# password = driver.find_element(By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup')
#
#
# email.click()
# action = ActionChains(driver)
# action.send_keys_to_element(email,'sultan.s.p.786.90@gmail.com').perform()
#
# password.click()
# action.send_keys_to_element(password,'Hornet@1999').perform()
#
# driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Log in"]/android.view.ViewGroup').click()

# driver.find_element(By.XPATH,'//android.widget.FrameLayout[@resource-id="com.facebook.lite:id/main_layout"]/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup[2]').click()
# driver.find_element(By.ID,'com.google.android.gms:id/credential_save_reject').click()
# driver.find_element(By.XPATH,'//android.widget.FrameLayout[@resource-id="com.facebook.lite:id/main_layout"]/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup[2]').click()
# driver.find_element(By.CLASS_NAME,'android.view.View').click()
# driver.find_element(By.CLASS_NAME,'android.view.View').click()
# driver.find_element(By.ID,'com.android.packageinstaller:id/permission_allow_button').click()
# driver.find_element(By.CLASS_NAME,'android.view.View').click()
# driver.find_element(By.CLASS_NAME,'android.view.View').click()

time.sleep(5)
driver.quit()