from locators.beon_locator import LocatorsBeonHome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class TestBeonHome:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.locators_beon_home = LocatorsBeonHome

    def test_click_join(self):
        driver = self.driver
        driver.get("https://beon.studio/")

        join_us_btn = driver.find_element(By.XPATH, self.locators_beon_home.join_us_btn_xpath)
        join_us_btn.click()

        selector_tech = Select(driver.find_element(By.CLASS_NAME, self.locators_beon_home.selector_tech_class))
        selector_tech.select_by_visible_text(self.locators_beon_home.text_tech_android)

        selector_job = Select(driver.find_element(By.XPATH, self.locators_beon_home.selector_job_xpath))
        selector_job.select_by_value(self.locators_beon_home.value_job_advertising)

        selector_role = Select(driver.find_element(By.XPATH, self.locators_beon_home.selector_role_xpath))
        selector_role.select_by_visible_text(self.locators_beon_home.text_role_ssr_engineering)

        oops_image = driver.find_element(By.XPATH, self.locators_beon_home.oops_img_xpath)
        assert oops_image, "IMAGE NOT FOUND"

        driver.close()