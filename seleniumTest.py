from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import os


class createBrowser:
    def selectDir(self):
        self.dir = './screenshots/'
        i = 0
        while True:

        

    def __init__(self, url):
        self.selectDir()
        self.driver = webdriver.PhantomJS()
        self.driver.get(url)

    def getPageData(self):
        return driver.page_source.encode('utf-8')

    def getNumOfPics(self):

    def takePicker(self):
        self.driver.save_screenshot("")

if __name__ == '__main__':
    url = sys.argv[1]
    browser = createBrowser(url)
    page = browser.getPageData()

