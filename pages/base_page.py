import allure
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def enter_on_button(self, locator_button):
        self.driver.find_element(*locator_button).send_keys(Keys.ENTER)

    def enter_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def go_to_site(self, url):
        self.driver.get(url)

    def find_element(self, locator, time=10):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator), message=f'Not found {locator}')

    def click_on_button(self, locator_button):
        self.driver.find_element(*locator_button).click()

    def check_current_url(self):
        return self.driver.current_url

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

