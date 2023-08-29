from selenium.webdriver.common.keys import Keys
from locators.locator import MainPage, Order
from helper import wait_element, click_element


class TestOrder:
    def test_order_one(self, browser):
        browser.get("https://qa-scooter.praktikum-services.ru/")
        browser.find_element(*MainPage.ORDER_DOWN).send_keys(Keys.ENTER)
        click_element(browser, *Order.LAST_NAME)
        browser.find_element(*Order.LAST_NAME).send_keys('Диана')
        wait_element(browser, *Order.FIRST_NAME)
        browser.find_element(*Order.FIRST_NAME).send_keys('Кос')
        browser.find_element(*Order.ADDRESS).send_keys('Советская 133')
        click_element(browser, *Order.METRO)
        click_element(browser, *Order.ST)
        browser.find_element(*Order.NUMBER).send_keys('89245674321')
        browser.find_element(*Order.NEXT).send_keys(Keys.ENTER)
        wait_element(browser, *Order.IMPORT_DATE)
        click_element(browser, *Order.IMPORT_DATE)
        click_element(browser, *Order.DATA_SELECTION)
        click_element(browser, *Order.RENT_DEADLINE)
        click_element(browser, *Order.DAY)
        click_element(browser, *Order.BLACK_STONE)
        browser.find_element(*Order.COMMENTS).send_keys('Быстроо')
        browser.find_element(*Order.ORDER).send_keys(Keys.ENTER)
        click_element(browser, *Order.WANT_TO_ORDER)
        click_element(browser, *Order.VIEW_ORDER_STATUS)
        successful_order = browser.find_element(*Order.COMING_TO_YOU)
        assert successful_order.is_displayed(), 'Вернулся ожидаемый на странице заказа элемент'

    def test_order_two(self, browser):
        browser.get("https://qa-scooter.praktikum-services.ru/")
        browser.find_element(*MainPage.ORDER_HIGH).send_keys(Keys.ENTER)
        click_element(browser, *Order.LAST_NAME)
        browser.find_element(*Order.LAST_NAME).send_keys('Маша')
        wait_element(browser, *Order.FIRST_NAME)
        browser.find_element(*Order.FIRST_NAME).send_keys('Крайнова')
        browser.find_element(*Order.ADDRESS).send_keys('Малиновского 1214')
        click_element(browser, *Order.METRO)
        click_element(browser, *Order.ST)
        browser.find_element(*Order.NUMBER).send_keys('89245675423')
        browser.find_element(*Order.NEXT).send_keys(Keys.ENTER)
        wait_element(browser, *Order.IMPORT_DATE)
        click_element(browser, *Order.IMPORT_DATE)
        click_element(browser, *Order.DATA_SELECTION)
        click_element(browser, *Order.RENT_DEADLINE)
        click_element(browser, *Order.DAY)
        click_element(browser, *Order.GREY)
        browser.find_element(*Order.COMMENTS).send_keys('Спасибо')
        browser.find_element(*Order.ORDER).send_keys(Keys.ENTER)
        click_element(browser, *Order.WANT_TO_ORDER)
        click_element(browser, *Order.VIEW_ORDER_STATUS)
        successful_order = browser.find_element(*Order.COMING_TO_YOU)
        assert successful_order.is_displayed(), 'Вернулся ожидаемый на странице заказа элемент'







