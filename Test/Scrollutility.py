from appium.webdriver.common.appiumby import AppiumBy



class ScrollUtil:

    @staticmethod
    def ScrollToTextByAndroidAutomator(text,driver):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                            "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains(\"" + text + "\").instance(0))").click()

    @staticmethod
    def swipeUp(howManySwipes, driver):
        for i in range(howManySwipes):
            driver.swipe(514,600,514,200,1000)

    @staticmethod
    def swipeDown(howManySwipes, driver):
        for i in range(howManySwipes):
            driver.swipe(514,500,514,800,1000)

    @staticmethod
    def swipeLeft(howManySwipes, driver):
        for i in range(howManySwipes):
            driver.swipe(900, 600, 200, 200, 1000)

    @staticmethod
    def swipeRight(howManySwipes, driver):
        for i in range(howManySwipes):
            driver.swipe(200, 600, 900, 600, 1000)
