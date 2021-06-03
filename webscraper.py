from selenium import webdriver as wd
from selenium.common.exceptions import ElementClickInterceptedException
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import random
import pyautogui

driver = wd.Firefox(executable_path="./geckodriver") # controls firefox
url = 'https://web.simple-mmo.com/login' # url of simple mmo website

# my username and password for simple mmo 
username = "caturix29@gmail.com"
passwd = "Timba123"

driver.get(url) # opens browser and website


def login():
	''' Function for logging into simple mmo '''
	password_input = driver.find_element_by_xpath("//input[@type='password']")
	password_input.send_keys(passwd)
	email_input = password_input.find_element_by_xpath(".//preceding::input[not(@type='hidden')]")
	email_input.send_keys(username)

	remember_checkbox = driver.find_element_by_xpath("//input[@type='checkbox']")
	remember_checkbox.click()

	login_button = driver.find_element_by_id("kt_login_signin_submit")
	login_button.click()


def quest():
	# check quest points
	quest_points = driver.find_element_by_id('current_quest_points')
	quest_points = int(quest_points.text)
	if quest_points > 0:
		# go to quest menu
		quest_menu_buttons = driver.find_elements_by_xpath("//a[@href='/quests/viewall']")
		quest_menu_buttons[1].click()
		# randomly choose a quest and do it n times (n=number of quest points)
		all_quests = driver.find_elements_by_xpath("//button[contains(text(), 'View Quest')]")
		for _ in range(quest_points):
			if len(all_quests)>1:
				random_quest = random.choice(all_quests)
			else:
				random_quest = random_quests[0]
			pyautogui.scroll(-10)
			try: # handling following error
				random_quest.click()
			except ElementClickInterceptedException: # sometimes show chat button overlays quest button
				pyautogui.scroll(-5)
				random_quest.click()
			# finish quest
			perform_quest_button = driver.find_element_by_xpath("//button[contains(text(), 'Perform quest')]")
			perform_quest_button.click()
			sleep(3) # sleep in order to let next menu load
			finish_quest_button = driver.find_element_by_xpath("//button[contains(text(), 'Finish Quest')]")
			finish_quest_button.click()


def goToHomeScreen():
	driver.get('https://web.simple-mmo.com/')


def battle():
	current_energy = driver.find_element_by_id('current_energy')
	current_energy = int(current_energy.text)
	if current_energy > 0:
		pass
		### TODO CONTINUE ### 





def main():
	login()
	quest()
	goToHomeScreen()
	battle()
	goToHomeScreen()
	#driver.quit()

main()
