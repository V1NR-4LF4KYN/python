'''
Selenium Test.

'''

# imports
from selenium import webdriver
#import selenium

PATH2 = "/home/pi/selenium/chromedriver"
PATH = "/usr/lib/chromium-browser/chromedriver"
driver = webdriver.Chrome(PATH)


def main():
    driver.get("www.gutefrage.net")
    #selenium.webdriver.title("www.gutefrage.net")

main()


