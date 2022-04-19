from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get('https://www.google.com/')
search = driver.find_element_by_xpath("//input[@name='q']")
search.send_keys("tma solution")
search.send_keys(Keys.ENTER)
tma = driver.find_element_by_xpath("//a[@href='https://www.tma.vn/']//h3")

if tma.is_displayed:
    print("tma is displayed and text is: ", tma.text)
else:
    print("tma not displayed")

driver.quit()