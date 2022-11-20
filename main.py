import selenium
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = selenium.webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
