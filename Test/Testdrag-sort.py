from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By

desired_capabilities = dict(
    deviceName='Android',
    platformName='Android',
    appPackage='com.mobeta.android.demodslv',
    appActivity='.Launcher',
    app='C:\\Users\\DefineLabs-PC\\PycharmProjects\\VCS-Control-Project\\Apk\\Drag-Sort.apk',
    automationName='UiAutomator2'

)
capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
driver.find_element(By.ID,'com.android.permissioncontroller:id/continue_button').click()
driver.find_element(By.ID,'android:id/button1').click()
driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.mobeta.android.demodslv:id/activity_desc" and @text="Use the menu to adjust settings related to item removal and drag initiation. These options are provided by the DragSortController class."]').click()

element = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.mobeta.android.demodslv:id/text" and @text="Brad Mehldau"]')
print(len(element))
# actions = ActionChains(driver)
# actions.