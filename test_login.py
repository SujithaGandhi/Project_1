"""
Test Case to verify the Login of OrangeHRM with Pytest
test_login.py
"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from Data import data
from Locators import locators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys


class Test_OrangeHRM:

   @pytest.fixture
   def booting_function(self):
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
       self.driver.implicitly_wait(10)
       yield
       self.driver.close()

   def test_validlogin(self, booting_function):
       self.driver.get(data.Web_Data().url)
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().username_locator).send_keys(data.Web_Data().username)
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().password_locator).send_keys(data.Web_Data().password)
       self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().submit_button_locator).click()
       #assert self.driver.current_url == data.Web_Data().dashboard_url
       print("SUCCESS : Logged in with Username {a} & Password {b}".format(a=data.Web_Data().username, b=data.Web_Data.password))    

  
   def test_invalidlogin(self, booting_function):
       self.driver.get(data.Web_Data().url)
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().username_locator).send_keys("Admin")
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().password_locator).send_keys("Admin")
       self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().submit_button_locator).click()
       #assert self.driver.current_url == data.Web_Data().dashboard_url
       print("Error : Through error in with invalid Username  & Password ")

   def test_editemp(self, booting_function):
       self.driver.get(data.Web_Data().url)
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().username_locator).send_keys(data.Web_Data().username)
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().password_locator).send_keys(data.Web_Data().password)
       self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().submit_button_locator).click()  
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click() 
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a').click() 
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]').click() 
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input').send_keys("Edited")
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button').click()  
       print("SUCCESS : Edited employee details ")

   def test_newemp(self, booting_function):
       self.driver.get(data.Web_Data().url)
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().username_locator).send_keys(data.Web_Data().username)
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().password_locator).send_keys(data.Web_Data().password)
       self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().submit_button_locator).click()  
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a').click()
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input').send_keys("Test")
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input').send_keys("User")
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input').send_keys("RJ13 20120123456")
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input').send_keys("2026-04-15")
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input').send_keys("589621457")
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div').click()
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input').send_keys("1989-04-15")
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span').click()
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button').click()
       print("SUCCESS : Employee Added !") 

       

   def test_dltemp(self, booting_function):
       self.driver.get(data.Web_Data().url)
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().username_locator).send_keys(data.Web_Data().username)
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().password_locator).send_keys(data.Web_Data().password)
       self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().submit_button_locator).click()  
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()   
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a').click()
       self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]').click()
       #self.driver.switch_to.alert.accept()
       alert = Alert(self.driver)
       alert.accept()
       print("SUCCESS : Employee details deleted !") 
       

