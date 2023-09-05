import allure
from selenium.webdriver import Keys
from locators.ya_scooter_main_page_locators import LocatorMainYaScooterPage
from locators.ya_scooter_order_page_locators import LocatorOrderYaScooterPage
from pages.base_page import BasePage


class YaScooterOrderPage(BasePage):


    def select_station(self, locator):
        a = self.driver.find_element(*locator)
        a.click()
        a.send_keys(Keys.DOWN)
        a.send_keys(Keys.ENTER)


    def select_current_date(self, locator):
        a = self.driver.find_element(*locator)
        a.click()
        a.send_keys(Keys.ENTER)


    def select_rental_period(self, locator, period_value):
        self.driver.find_element(*locator).click()
        self.driver.find_element(*period_value).click()

    def get_text_successful_order(self):
        return self.get_text(LocatorOrderYaScooterPage.SUCCESSFUL_ORDER)

    def get_text_block_with_questions(self):
        return self.get_text(LocatorMainYaScooterPage.BLOCK_WITH_QUESTIONS)

    def enter_on_button_order_in_header(self):
        self.enter_on_button(LocatorMainYaScooterPage.ORDER_BUTTON_IN_HEADER)

    def click_on_button_scooter(self):
        self.click_on_button(LocatorOrderYaScooterPage.SCOOTER_BUTTON)

    def fill_field_for_order_via_top_button(self):
        self.enter_on_button_order_in_header()
        self.enter_text(LocatorOrderYaScooterPage.FIRST_NAME, "Иван")
        self.enter_text(LocatorOrderYaScooterPage.LAST_NAME, "Иванов")
        self.enter_text(LocatorOrderYaScooterPage.ADDRESS, "г. Ростов, д. 98")
        self.select_station(LocatorOrderYaScooterPage.STATION)
        self.enter_text(LocatorOrderYaScooterPage.PHONE_NUMBER, "+79876543434")
        self.enter_on_button(LocatorOrderYaScooterPage.BUTTON_NEXT)

        self.select_current_date(LocatorOrderYaScooterPage.DELIVERY_DATE)
        self.select_rental_period(LocatorOrderYaScooterPage.RENTAL_PERIOD, LocatorOrderYaScooterPage.RENTAL_PERIOD_VALUE_1)
        self.click_on_button(LocatorOrderYaScooterPage.SCOOTER_BLACK_COLOR_CHECKBOX)
        self.enter_text(LocatorOrderYaScooterPage.COMMENT, "Жду заказ")
        self.enter_on_button(LocatorOrderYaScooterPage.BUTTON_ORDER_MIDDLE)
        self.enter_on_button(LocatorOrderYaScooterPage.BUTTON_ORDER_YES)

    def fill_field_for_order_via_middle_button(self):
        self.enter_on_button(LocatorMainYaScooterPage.ORDER_BUTTON_IN_MIDDLE)
        self.enter_text(LocatorOrderYaScooterPage.FIRST_NAME, "Мария")
        self.enter_text(LocatorOrderYaScooterPage.LAST_NAME, "Георгиевна")
        self.enter_text(LocatorOrderYaScooterPage.ADDRESS, "г. Нальчик, д. 100")
        self.select_station(LocatorOrderYaScooterPage.STATION)
        self.enter_text(LocatorOrderYaScooterPage.PHONE_NUMBER, "+79870545606")
        self.enter_on_button(LocatorOrderYaScooterPage.BUTTON_NEXT)

        self.select_current_date(LocatorOrderYaScooterPage.DELIVERY_DATE)
        self.select_rental_period(LocatorOrderYaScooterPage.RENTAL_PERIOD, LocatorOrderYaScooterPage.RENTAL_PERIOD_VALUE_2)
        self.click_on_button(LocatorOrderYaScooterPage.SCOOTER_GREY_COLOR_CHECKBOX)
        self.enter_text(LocatorOrderYaScooterPage.COMMENT, "Спасибо")
        self.enter_on_button(LocatorOrderYaScooterPage.BUTTON_ORDER_MIDDLE)
        self.enter_on_button(LocatorOrderYaScooterPage.BUTTON_ORDER_YES)