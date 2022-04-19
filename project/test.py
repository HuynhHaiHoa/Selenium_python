from time import sleep
from POM.TestPage import HomePage, LoginPage
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture(params =[1,2] ,scope ='class')
def set_browser(request):
    if request.param == 1:
        driver = webdriver.Chrome()
    if request.param == 2:
        driver = webdriver.Firefox()
    request.cls.driver = driver 

@pytest.mark.usefixtures("set_browser")
class BasicTest:
    pass


@pytest.mark.suite("suite1")
class TestSuite2(BasicTest):

    def testcase1(self):
        driver = self.driver
        loginpage = LoginPage(driver)
        homepage = HomePage(driver)

        loginpage.login("http://demo.guru99.com/V4/","mgr123", "mgr!23")
        homepage.verifyLogin()
