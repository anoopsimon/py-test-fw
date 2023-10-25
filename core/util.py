from selenium.webdriver.common.by import By

def get_element_text(driver, locator):
    try:
        element = driver.find_element(By.CSS_SELECTOR, locator)  # You can change the locator method (By) as needed
        print("element")
        return element.text
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None  # Return None in case of any error