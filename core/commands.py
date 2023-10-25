import re
from selenium.webdriver.common.by import By

class Commands:
  def __init__(self,driver):
    self.driver = driver

  def goto(self,url):
    print(f'Navigating to url {url}')
    self.driver.get(url)
    
  def find_element_by_locator(self, locator):
        if re.match(r'^//', locator):
            return self.driver.find_element(By.XPATH, locator)
        elif re.match(r'^[a-zA-Z0-9\[\]=#.\-_ ]+$', locator):
            return self.driver.find_element(By.CSS_SELECTOR, locator)
        else:
            raise ValueError("Invalid locator format. Use valid XPath or CSS Selector.")


  def type(self, locator, value):
        element = self.find_element_by_locator(locator)
        element.clear()
        element.send_keys(value)

  def type_special_key(self, locator, special_key):
        element = self.find_element_by_locator(locator)
        element.clear()
        element.send_keys(special_key)