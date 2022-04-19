from POM.webdriver import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def login(self, url, username, password):
        xpath_username = (By.XPATH, "//input[@name='uid']")
        xpath_password = (By.XPATH, "//input[@name='password']")
        xpath_login_btn = (By.XPATH, "//input[@name='btnLogin']")
       
        self.driver.get(url)
        self.enter_text(xpath_username, username)
        self.enter_text(xpath_password, password)
        self.click(xpath_login_btn)


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def verifyLogin(self):
        expected_title = " Guru99 Bank Manager HomePage "
        assert (self.get_title, expected_title)

class HUSCPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def login(self, url, username, password):
        xpath_username = (By.XPATH, "//input[@name='loginID']")
        xpath_password = (By.XPATH, "//input[@name='password']")
        xpath_login_btn = (By.XPATH, "//button[@type='submit']")
       
        self.driver.get(url)
        self.enter_text(xpath_username, username)
        self.enter_text(xpath_password, password)
        self.click(xpath_login_btn)