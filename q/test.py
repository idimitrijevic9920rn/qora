from selenium import webdriver

import time
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from _csv import reader
from sys import exit
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def Connecting_To_Browser(id_str, pass_str):
    if id_str != "" and pass_str != "":
        driver = webdriver.Chrome();
        driver.get('http://quora.com/')

        with open("accounts.ini", 'r') as f:
            doc = f.read().split('\n')
            print(doc)

        form = driver.find_element_by_class_name('regular_login')
        email = form.find_element_by_name("email")
        email.send_keys("id_str")
        password = form.find_element_by_name("password")
        password.send_keys("pass_str")
        password.send_keys(Keys.RETURN)
        time.sleep(3)

        driver.execute_script("window.a = document.getElementsByClassName('submit_button ignore_interaction');")

        driver.get('https://www.quora.com/profile/Elena-Ruiz-14')
        time.sleep(2)

        upvotes = driver.find_elements_by_id('upvote')
        for up in upvotes:
            up.click()




with open('mejlovi.csv','r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)

total_len = len(list_of_rows)
ids_pass_list = list_of_rows

for i in range(len(ids_pass_list)):
    id_str = ids_pass_list[i][0]
    id_pass = ids_pass_list[i][1]
    print(i)
    print("Login Id: ", id_str)
    print("Login Password: ", id_pass)
    Connecting_To_Browser(id_str, id_pass)












