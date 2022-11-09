import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pageObjects.Loginpage import LoginPage
from Utilities.readproperties import ReadConfig
from Utilities.customlogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getapplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()

    logger = LogGen.loggen()

    def test_homepagetitle(self,setup):
        self.logger.info("****Test_001_Login******")
        self.logger.info("****verifying homepage title******")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login1":
            print("actual_title is matched")
            self.logger.info("****homepage title test is passed ******")
        else:
            self.driver.save_screenshot("C:\\Users\\DELL\\PycharmProjects"
                                        "\\pom-project\\Screenshots"+"test_homepagetitle.png")
            print("home page title is not matched")
            self.logger.info("****homepage title test is failed ******")
        self.driver.close()

    def test_login(self,setup):
        self.logger.info("****verifying login page ******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.enterusername(self.username)
        time.sleep(1)
        self.lp.enterpassword(self.password)
        time.sleep(1)
        self.lp.clicklogin()
        time.sleep(3)
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            print("dashboard is matched")
            self.driver.save_screenshot(".\\screenshots"+ "test_login.png")
            self.logger.info("**** login page test is passed******")
        else:
            print("page isn't matched")
        self.lp.clicklogout()
        self.driver.close()
        self.logger.info("**** login page test is failed******")





