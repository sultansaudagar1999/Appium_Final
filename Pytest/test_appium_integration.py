import time

import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver import appium_service
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_data():
    return [

        ["Iphone 15"],
        ["Iphone 15 Pro Max"],

    ]
@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)


def setup_function():
    global appium_service
    appium_service = AppiumService()
    appium_service.start()

    desired_capabilities = dict(
        deviceName='Android',
        platformName='Android',
        app='C:\\Users\\DefineLabs-PC\\PycharmProjects\\VCS-Control-Project\\Apk\\Amazon.apk',
        automationName='UiAutomator2',
        appPackage='com.amazon.mShop.android.shopping',
        appActivity='com.amazon.mShop.home.HomeActivity'

    )
    capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)
    global driver
    driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
    driver.implicitly_wait(5)


def teardown_function():
    time.sleep(2)
    driver.quit()
    appium_service.stop()

@pytest.mark.parametrize("Search_Parameter", get_data())
def test_search(Search_Parameter):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, 'com.amazon.mShop.android.shopping:id/chrome_search_hint_view')))
    driver.find_element(By.ID, 'com.amazon.mShop.android.shopping:id/chrome_search_hint_view').click()
    driver.find_element(By.ID, 'com.amazon.mShop.android.shopping:id/rs_search_src_text').send_keys(Search_Parameter)
    driver.press_keycode(66)
    time.sleep(2)
    # allure.attach(driver.get_screenshot_as_png(),name="screenshot",attachment_type=AttachmentType.PNG)


