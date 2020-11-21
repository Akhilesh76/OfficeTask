from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver.exe")
driver.get("https://www.propertycapsule.com/")
driver.implicitly_wait(10)

#web page scroll
driver.execute_script("window.scrollBy(0,2000)","")

#click on see for yourself button
driver.find_element_by_link_text("See for yourself").click()

#To verify checkbox is enabled or not
driver.find_element_by_xpath("//*[@id='GDPR_Opt_In__c']").is_enabled()
print(driver.find_element_by_xpath("//*[@id='GDPR_Opt_In__c']").is_enabled())

#Click on checkbox
driver.find_element_by_xpath("//*[@id='GDPR_Opt_In__c']").click()