__author__ = "Shantam Mathuria"
__copyright__ = "Copyright 2018"
__credits__ = ["Shantam Mathuria"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Shantam Mathuria"
__email__ = "shantam.m22@gmail.com"
__status__ = "Production"

import time
from _csv import reader
import csv

from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sys import exit


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




