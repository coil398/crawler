from selenium import webdriver
import sys
import os
from datetime import datetime


class createBrowser:
    logs = list()
    _baseDir = './screenshots/'

    def createPicPath(self, num):
        return self._baseDir + 'pic-' + str(num) + '.jpg'

    def getNumOfFiles(self):
        i = 0
        while True:
            path = self.createPicPath(i)
            print('path: ' + path)
            if os.path.exists(path):
                i = i + 1
            else:
                return i

    def setNumOfPics(self):
        self.numOfPics = self.getNumOfFiles()
        print('numOfPics: ' + str(self.numOfPics))

    def __init__(self, url):
        self.setNumOfPics()
        self.driver = webdriver.PhantomJS()
        print('getting page data with the url: ' + url)
        self.driver.get(url)
        self.logs.append(datetime.now().strftime(
            '%Y/%m/%d %H:%M:%S') + ' : ' + 'got page data with the url: ' + url)
        print('done...')

    def getPageData(self):
        return self.driver.page_source.encode('utf-8')

    def takeScreenshot(self):
        path = self.createPicPath(self.numOfPics)
        print('path' + path)
        self.driver.save_screenshot(path)
        self.logs.append(
            datetime.now().strftime('%Y/%m/%d %H:%M:%S') + ' : ' + 'saved a screenshot with the path: ' + path)
        self.numOfPics = self.numOfPics + 1

    def saveLog(self):
        print('saving the logs...')
        with open('crawler.log', mode='a', encoding='utf-8') as f:
            f.write('\n')
            for log in self.logs:
                print(log)
                f.write(log + '\n')
        print('done...')

    def quit(self):
        self.driver.quit()
        print('quitted crawling')


def createDirIfNotExists():
    if os.path.exists('./screenshots'):
        pass
    else:
        os.makedirs('./screenshots')
    return


def createBrowsers():
    browsers = list()
    with open('./url.list', 'r') as f:
        for line in f:
            browsers.append(line)
    return browsers


def getLinesOfFile():
    return sum(1 for line in open('./url.list'))


def checkExistenceOfValidFile():
    if os.path.exists('./url.list'):
        if getLinesOfFile() > 0:
            return True
        else:
            return False
    else:
        return False


def useBrowser(url):
    browser = createBrowser(url)
    browser.takeScreenshot()
    browser.saveLog()
    browser.quit()


def useBrowsers():
    browsers = createBrowsers()
    for browser in browsers:
        useBrowser(url)


if __name__ == '__main__':
    createDirIfNotExists()
    if len(sys.argv) > 1:
        url = sys.argv[1]
        useBrowser(url)
    else:
        if checkExistenceOfValidFile():
            useBrowsers()
        else:
            print('A Valid File For URLS Is In Need.')
