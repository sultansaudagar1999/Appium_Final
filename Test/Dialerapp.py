from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By

desired_capabilities = dict(
    deviceName='Android',
    platformName='Android',
    appPackage='com.samsung.android.dialer',
    appActivity='.DialtactsActivity t382',
    automationName='UiAutomator2'

)
capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)

driver.find_element(By.ID,'com.samsung.android.dialer:id/nine').click()
driver.find_element(By.ID,'com.samsung.android.dialer:id/seven').click()
driver.find_element(By.ID,'com.samsung.android.dialer:id/six').click()
driver.find_element(By.ID,'com.samsung.android.dialer:id/two').click()
driver.find_element(By.ID,'com.samsung.android.dialer:id/six').click()
driver.find_element(By.ID,'com.samsung.android.dialer:id/two').click()
driver.find_element(By.ID,'com.samsung.android.dialer:id/eight').click()
driver.find_element(By.ID,'com.samsung.android.dialer:id/three').click()
driver.find_element(By.ID,'com.samsung.android.dialer:id/seven').click()
driver.find_element(By.ID,'com.samsung.android.dialer:id/two').click()


driver.find_element(By.ID,'com.samsung.android.dialer:id/dialButtonImage').click() #Dial Button