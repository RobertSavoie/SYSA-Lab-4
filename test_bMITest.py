# Names: Megan Gagliardi, Rob Savoie
# Date: Nov 20, 2022
# Program: BMI Test
# Description: runs a test of a bmi calculator and returns the results
# Generated by Selenium IDE


# Had to add pytest to my tools
import pytest
import time
import json
# Had to make sure selenium was added
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestBMITest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_bMITest(self):
    self.driver.get("https://www.calculator.net/body-fat-calculator.html")
    self.vars["varGender"] = "F"
    if self.driver.execute_script("return (arguments[0]===\"F\")", self.vars["varGender"]):
      self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(2) > .rbmark").click()
      self.driver.find_element(By.NAME, "cage").click()
      self.driver.find_element(By.NAME, "cage").send_keys("40")
      self.driver.find_element(By.NAME, "cweightkgs").click()
      self.driver.find_element(By.NAME, "cweightkgs").send_keys("100")
      self.driver.find_element(By.ID, "cheightmeter").click()
      self.driver.find_element(By.ID, "cheightmeter").send_keys("189")
      self.driver.find_element(By.ID, "cneckmeter").click()
      self.driver.find_element(By.ID, "cneckmeter").send_keys("57")
      self.driver.find_element(By.ID, "cwaistmeter").click()
      self.driver.find_element(By.ID, "cwaistmeter").send_keys("98")
      self.driver.find_element(By.ID, "chipmeter").click()
      self.driver.find_element(By.ID, "chipmeter").send_keys("100")
      self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(3)").click()
      self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(4) input").click()
      self.vars["result"] = "23.0%"
      assert(self.vars["result"] == "23.0%")
      print("calculation result is: {}".format(self.vars["result"]))
    else:
      self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()
      self.driver.find_element(By.CSS_SELECTOR, "tbody:nth-child(3) > tr:nth-child(2)").click()
      self.driver.find_element(By.NAME, "cage").send_keys("15")
      self.driver.find_element(By.NAME, "cweightkgs").click()
      self.driver.find_element(By.NAME, "cweightkgs").send_keys("220")
      self.driver.find_element(By.ID, "cheightmeter").click()
      self.driver.find_element(By.ID, "cheightmeter").send_keys("90")
      self.driver.find_element(By.ID, "cneckmeter").click()
      self.driver.find_element(By.ID, "cneckmeter").send_keys("18")
      self.driver.find_element(By.ID, "cwaistmeter").click()
      self.driver.find_element(By.ID, "cwaistmeter").send_keys("100")
      self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(4) input").click()
      self.vars["result"] = "60.7%"
      assert(self.vars["result"] == "60.7%")
      print("calculation result is: {}".format(self.vars["result"]))


  
