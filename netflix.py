from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pymsgbox
from datetime import datetime
now = datetime.now()
s1 = str(now.strftime("%H:%M:%S"))

driver = webdriver.Chrome()
vars = {}


driver.get("https://www.netflix.com/in/login")
driver.find_element(By.CSS_SELECTOR, ".nfEmailPhoneControls .placeLabel").click()
driver.find_element(By.ID, "id_userLoginId").send_keys("UsernameHere")
driver.find_element(By.ID, "id_password").click()
driver.find_element(By.ID, "id_password").send_keys("passwordhere")
driver.find_element(By.CSS_SELECTOR, ".login-remember-me-label-text").click()
driver.find_element(By.CSS_SELECTOR, ".login-button").click()
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".profile:nth-child(2) .profile-icon"))
    )
driver.find_element(By.CSS_SELECTOR, ".profile:nth-child(2) .profile-icon").click()
time.sleep(3)
driver.find_element_by_class_name('searchBox').click()
driver.find_element(By.CSS_SELECTOR, "input").click()
driver.find_element(By.CSS_SELECTOR, "input").send_keys("Friends")
driver.find_element(By.CSS_SELECTOR, "input").send_keys(Keys.ENTER)
driver.get('https://www.netflix.com/watch/70274015?trackId=13752289&tctx=0%2C0%2C7ae1ec6455c6505fefe4e6c1dce8967c13395af2%3Afa3dd29552f1d9a54f6eaeca4ebcad06eebe6e16%2C%2C')


cs="0:00:40"
while True:

	now = datetime.now()
	s2 = str(now.strftime("%H:%M:%S"))
	tdelta = datetime.strptime(s2, '%H:%M:%S') - datetime.strptime(s1, '%H:%M:%S')
	if(str(tdelta)==cs):
		pymsgbox.alert('You have watched netflix for an Hour!', 'Alert')
		s1=s2
