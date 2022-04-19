import selenium
import time
from selenium import webdriver
import csv
from csv import reader


def Connecting_To_Browser(id_str, pass_str):
    if id_str != "" and pass_str != "":
        browser = webdriver.Chrome(executable_path='./drivers/chromedriver')
        try:
            browser.get('https://www.gmail.com/')

            email_field = browser.find_element_by_id("identifierId")
            email_field.clear()

            email_field.send_keys(id_str)

            email_next_button = browser.find_element_by_xpath("//div[@class='qhFLie']//button")
            email_next_button.click()

            time.sleep(2)

            password_field = browser.find_element_by_name("password")
            password_field.clear()

            password_field.send_keys(pass_str)

            password_next_button = browser.find_element_by_xpath("//div[@class='qhFLie']//button")
            password_next_button.click()

            time.sleep(3)

            browser.quit()
        except:
            browser.quit()
    else:
        print("Either ID or PASSWORD is null")


with open('D:\TMA Solution\Selenium_Python\Selenium_project\email.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)

print("Total Ids and Passwords: ", len(list_of_rows))
total_Len = len(list_of_rows)

ids_pass_list = list_of_rows

for i in range(len(ids_pass_list)):
    i = i + 1
    id_str = ids_pass_list[i][0]
    id_pass = ids_pass_list[i][1]
    print(i)
    print("Login Id: ", id_str)
    print("Login Password: ", id_pass)

    Connecting_To_Browser(id_str, id_pass)
