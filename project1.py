from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    #Verify title of web page
    def page_title(self):
        self.driver.get("https://www.propertycapsule.com/")
        self.assertEqual("propertycapsule",self.driver.title,"not matching")

    def test_login(self):
        self.driver.get("https://www.propertycapsule.com/")
        self.driver.implicitly_wait(10)

        #click on Signup/Login
        self.driver.find_element_by_link_text("Deal Maker Signup/Login").click()

        #pass the input username
        self.driver.find_element_by_xpath(
            "/html/body/app-root/app-marqetmap-app/app-map/app-popup/app-signup/div/div/perfect-scrollbar/div/div[1]/div/div[1]/form/div[4]/div/input").send_keys(
            "singhakhilesh795@gmail.com")

        #pass the input password
        self.driver.find_element_by_css_selector(
            "body > app-root > app-marqetmap-app > app-map > app-popup > app-signup > div > div > perfect-scrollbar > div > div.ps-content > div > div.form-wrapper > form > div:nth-child(5) > input").send_keys(
            "India@12")

        #click on continue
        self.driver.find_element_by_xpath(
            "/html/body/app-root/app-marqetmap-app/app-map/app-popup/app-signup/div/div/perfect-scrollbar/div/div[1]/div/div[1]/form/div[6]/div").click()

        #input the name
        self.driver.find_element_by_css_selector(
            "body > app-root > app-marqetmap-app > app-map > app-popup > app-signup > div > div > perfect-scrollbar > div > div.ps-content > div > div.form-wrapper > form > div:nth-child(2) > div > input").send_keys(
            "Akhilesh Singh")

        #input the company name
        self.driver.find_element_by_css_selector(
            "body > app-root > app-marqetmap-app > app-map > app-popup > app-signup > div > div > perfect-scrollbar > div > div.ps-content > div > div.form-wrapper > form > div:nth-child(3) > div > input").send_keys(
            "decimal")

        #input mobile no
        self.driver.find_element_by_css_selector(
            "body > app-root > app-marqetmap-app > app-map > app-popup > app-signup > div > div > perfect-scrollbar > div > div.ps-content > div > div.form-wrapper > form > div:nth-child(4) > div > input").send_keys(
            "8368180978")

        #click on send me a code button
        self.driver.find_element_by_xpath(
            "/html/body/app-root/app-marqetmap-app/app-map/app-popup/app-signup/div/div/perfect-scrollbar/div/div[1]/div/div[2]/form/div[5]").click()

        #A page will be open to enter the otp

if __name__=='__main__':
    unittest.main()