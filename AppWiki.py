from selenium import webdriver
from Pages.WikiMainPage import WikiMainHelper

class App:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wiki = WikiMainHelper(self)

    def open_wiki_page(self):
        driver = self.driver
        driver.get("https://en.wikipedia.org/wiki/Main_Page")

    def destroy(self):
        self.driver.quit()