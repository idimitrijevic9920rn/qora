from selenium import webdriver
import time
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys
from _csv import reader
import os
from sys import exit
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import random

def Connecting_To_Browser(id_str, pass_str, pproxy):
    if id_str != "" and pass_str != "" and pproxy != "":
        print(id_str)
        proxy_ip_port = pproxy
        proxy = Proxy()
        proxy.proxy_type = ProxyType.MANUAL
        proxy.http_proxy = proxy_ip_port
        proxy.ssl_proxy = proxy_ip_port
        capabilities = webdriver.DesiredCapabilities.CHROME
        proxy.add_to_capabilities(capabilities)
        driver = webdriver.Chrome(desired_capabilities=capabilities)
        driver.get('http://quora.com/')
        time.sleep(8)
        email = driver.find_element_by_id("email")
        email.send_keys(id_str)
        password = driver.find_element_by_id("password")
        password.send_keys(pass_str)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        driver.execute_script("window.a = document.getElementsByClassName('submit_button ignore_interaction');")

        driver.get('https://www.quora.com/How-can-I-view-deleted-Instagram-dms/answer/Bet-Richards')
        time.sleep(2)
        upvotes = driver.find_elements_by_id('upvote')
        for up in upvotes:
            up.click()
        time.sleep(random.randint(10, 15))

        driver.quit()

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')

with open('mejlovi.csv','r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)

total_len = len(list_of_rows)
ids_pass_list = list_of_rows

for i in range(len(ids_pass_list)):
    id_str = ids_pass_list[i][0]
    id_pass = ids_pass_list[i][1]
    id_ip = ids_pass_list[i][2]
    time.sleep(3)
    Connecting_To_Browser(id_str, id_pass,id_ip)
















