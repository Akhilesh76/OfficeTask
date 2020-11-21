from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver.exe")
#navigate to url
driver.get("https://www.propertycapsule.com/")
driver.implicitly_wait(10)

# Click on Signup/Login button
driver.find_element_by_link_text("Deal Maker Signup/Login").click()

#click on close button
driver.find_element_by_xpath("/html/body/app-root/app-marqetmap-app/app-map/app-popup/app-signup/div/div/i").click()

#click on places elements
driver.find_element_by_xpath("//*[@id='maps-layers-sidebar']/div/div[5]/div[2]").click()

#Verify checkbox is enabled or not
print(driver.find_element_by_class_name("control-indicator").is_enabled())

#click on checkboxes
driver.find_element_by_css_selector("#maps-layers-sidebar > div > app-place-filter > div > perfect-scrollbar > div > div.ps-content > div:nth-child(6) > label > label").click()
driver.find_element_by_css_selector("#maps-layers-sidebar > div > app-place-filter > div > perfect-scrollbar > div > div.ps-content > div:nth-child(3) > label > label").click()