#   author: korayuzun22@gmail.com

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service = service)

driver.get("https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fspmallick%2Flearnopencv")
while(True):
    pass