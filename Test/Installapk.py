import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_capabilities = dict(
    deviceName='Android',
    platformName='Android',
    app='C:\\Users\\DefineLabs-PC\\PycharmProjects\\VCS-Control-Project\\Apk\\Amazon.apk',
    automationName='UiAutomator2',
    appPackage='com.amazon.mShop.android.shopping',
    appActivity='com.amazon.mShop.home.HomeActivity'

)
capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
driver.implicitly_wait(5)

wait = WebDriverWait(driver,10)
wait.until(EC.element_to_be_clickable((By.ID,'com.amazon.mShop.android.shopping:id/chrome_search_hint_view')))
driver.find_element(By.ID,'com.amazon.mShop.android.shopping:id/chrome_search_hint_view').click()
driver.find_element(By.ID,'com.amazon.mShop.android.shopping:id/rs_search_src_text').send_keys("Iphone 15")
driver.press_keycode(66)


# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("search").instance(0))').click()



time.sleep(5)
driver.quit()





