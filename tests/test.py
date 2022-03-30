from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from locators.home_page import LocatorsHomePage


class TestHome:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.locators = LocatorsHomePage

    def test_home(self):
        driver = webdriver.Chrome()
        driver.get("https://www.amazon.com")
        driver.implicitly_wait(3)
        home_logo = driver.find_element(By.ID, self.locators.logo_home_id)
        assert home_logo, "LOGO NOT FOUND"

        input_text = driver.find_element(By.ID, self.locators.search_bar_id)
        input_text.send_keys("PlayStation 5")
        input_text.send_keys(Keys.ENTER)

        # my_element = driver.find_element(By.XPATH, self.locators.home_nav_bar_option_xpath)
        # assert my_element.text == self.locators.nav_bar_option_text
        driver.quit()
