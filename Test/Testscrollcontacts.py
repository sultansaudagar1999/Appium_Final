from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

desired_capabilities = dict(
    deviceName='Android',
    platformName='Android',
    appPackage='com.samsung.android.app.contacts',
    appActivity='com.samsung.android.contacts.contactslist.PeopleActivity',
    automationName='UiAutomator2'

)
capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)

# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Vi Offers").instance(0))').click()

#Swipe Up
driver.swipe(514,600,514,200,1000)
driver.swipe(514,600,514,200,1000)
driver.swipe(514,600,514,200,1000)
driver.swipe(514,600,514,200,1000)

#Swipe Down
driver.swipe(514,500,514,800,1000)
driver.swipe(514,500,514,800,1000)
driver.swipe(514,500,514,800,1000)
driver.swipe(514,500,514,800,1000)