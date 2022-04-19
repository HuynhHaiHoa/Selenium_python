from selenium import webdriver

class TestPOMBase(object):
    def setup(self):
        request = self._funcargs.get('request')
        self.params = request._funcargs.get('params')
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')

    def teardown(self):
        self.driver.close()
        self.driver.quit()