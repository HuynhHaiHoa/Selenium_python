from POM.TestPage import HomePage, LoginPage, HUSCPage
from Data_driven_project.test_pom_base import TestPOMBase
import pytest

@pytest.mark.usefixtures("data_set")
class TestSuite2(TestPOMBase):

    def testcase1(self):
        driver = self.driver
        loginpage = LoginPage(driver)
        homepage = HomePage(driver)

        loginpage.login(self.params["url"],self.params["username"],self.params["passwd"])
        homepage.verifyLogin()
    
    def testcase2(self):
        driver = self.driver
        huscpage = HUSCPage(driver)

        huscpage.login(self.params["url"],self.params["username"],self.params["passwd"])