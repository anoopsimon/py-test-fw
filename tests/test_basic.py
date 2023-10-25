import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pytest_html_reporter import attach
from core.commands import Commands

class ChromeSearch(unittest.TestCase):
     def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(chrome_options)
        #self.driver = webdriver.Chrome("")

     def test_search_in_python_org(self):
        commands = Commands(self.driver)
        commands.goto('https://www.python.org')
        self.assertIn("Python", self.driver.title)
        commands.type("#id-search-field","getting started with python")
        #commands.type_special_key("#id-search-field",Keys.RETURN)
        #assert "https://www.python.org/search/?q=getting+started+with+python&submit=" == self.driver.current_url

      #   elem.send_keys(Keys.RETURN)
      #   get_element_text(driver,"id-search-field")
        attach(data=self.driver.get_screenshot_as_png())

     def test_GoogleSearchTest(self):
         commands = Commands(self.driver)
         commands.goto('https://www.google.com')
         commands.type('#APjFqb','Google')
      

def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
        unittest.main()
