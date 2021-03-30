# -*- coding: utf-8 -*-
# @Author: Chao
# @Date:   2018-08-23 22:57:28
# @Last Modified by:   Chao
# @Last Modified time: 2018-11-02 10:04:50

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import pandas as pd
import random
import time
import sys


class CreateGmail:
    """Auto Create Gmail Accounts with popular names"""

    def __init__(self, firstname, lastname, username, pswd):
        self._firstname = firstname
        self._lastname = lastname
        self._username = username
        self._pswd = pswd
        self._Donefile = open("./data/CreatedAccounts.csv", "a")
        self.Initialize()

    def Initialize(self):
        self._browser = webdriver.Chrome()
        self._browser.delete_all_cookies()
        self._browser.get("https://quora.com")
        signupButton = self._browser.find_element_by_class_name("signup_email_link")
        signupButton.click()

    def CreateAccount(self):
        # self.SetRecoveryEmail()

        firstName = self._browser.find_element_by_name('first_name')
        firstName.send_keys(self._firstname)
        time.sleep(1)
        lastName = self._browser.find_element_by_name('last_name')
        lastName.send_keys(self._lastname)
        time.sleep(1)
        email = self._browser.find_element_by_name('email')
        email.send_keys(self._username + '@gmail.com')
        time.sleep(1)
        password = self._browser.find_element_by_name('password')
        password.send_keys('Icr13357')
        time.sleep(3000)

    @staticmethod
    def GetUserInfo(firstnamefile, lastnamefile):
        FirstName = pd.read_csv(firstnamefile).sample(frac=1)
        LastName = pd.read_csv(lastnamefile).sample(frac=1)
        num = min(len(FirstName), len(LastName))
        if len(FirstName) > len(LastName):
            UserInfo = LastName
            UserInfo["firstname"] = FirstName.values[:num]
        else:
            UserInfo = FirstName
            UserInfo["lastname"] = LastName.values[:num]
        UserInfo.index = range(num)
        UserInfo.dropna()
        suffix = ""
        for i in range(6):
            suffix += str(random.randint(0, 9))
        UserInfo["username"] = UserInfo["firstname"] + UserInfo["lastname"] + suffix
        UserInfo["pswd"] = "super" + UserInfo["firstname"] + "233"
        return UserInfo

    def RunAppsScript(self, sharedlink):
        self._browser.get(sharedlink)
        time.sleep(10)

if __name__ == "__main__":
    firstnamefile = "./data/CSV_Database_of_First_Names.csv"
    lastnamefile = "./data/CSV_Database_of_Last_Names.csv"
    UserInfoDF = CreateGmail.GetUserInfo(firstnamefile, lastnamefile)
    for num in range(len(UserInfoDF)):
        UserInfoSeries = UserInfoDF.loc[num]
        CGM = CreateGmail(*UserInfoSeries)
        CGM.CreateAccount()
        # CGM.RunAppsScript(SharedScript)

