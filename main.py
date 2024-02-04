#   author: korayuzun22@gmail.com

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from getpass import getpass

# Chrome browser and driver must be same version. You can check your chrome version in: 
# Setting(triple dots) >> Help >> About Google Chrome
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service = service)

# link to go/test
driver.get("https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fspmallick%2Flearnopencv")

# for maximize window
driver.maximize_window()

# get current url
current_url = driver.current_url
print("Current url:" + current_url)

# get current tittle of page (html title)
title = driver.title
print("Current tittle:" + title)

# Select username button
username = driver.find_element(By.ID, "login_field")

# Get user name from user
username_user = input(" \n\n\n\nEnter User Name :")

# Write user name to user name block
username.send_keys(username_user)

# Select password button 
password = driver.find_element(By.ID, "password")

# Get pasword from user
password_user = getpass("\nEnter Password (your password hidden) ")

# Write to user password to password block
password.send_keys(password_user)

password.send_keys(Keys.ENTER)

# driver.get("https://youtube.com")
# current_url = driver.current_url
# print("Current url:" + current_url)

# # get current tittle of page (html title)
# title = driver.title
# print("Current tittle:" + title)

# save screen shot
# driver.save_screenshot("./screenshot/deneme.png")

# driver.back
# driver.forward
# driver.refresh
# driver.quit  # close browser
# driver.close # close window

# for waiting to page 
while(True):
    # TODO: add keyboard intterupt
    pass