import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators import MainPage
from helper import wait_element, click_element
questions = [
    [*MainPage.SCOOTER_PRICE, *MainPage.ASSERT_SCOOTER_PRICE, 'Вывод цен'],
             [*MainPage.SEVERAL_SCOOTER, *MainPage.SEVERAL_SCOOTER, 'Информация по нескольким самокатам'],
             [*MainPage.RENTAL_TIME, *MainPage.ASSERT_RENTAL_TIME, 'Информация по времени аренды'],
             [*MainPage.ORDER_A_SCOOTER_TODAY, *MainPage.ASSERT_ORDER_A_SCOOTER_TODAY, 'Информация по аренде сегодня'],
             [*MainPage.CHARGING_IS_PROVIDED, *MainPage.ASSERT_CHARGING_IS_PROVIDED, 'Информация по зарядке'],
             [*MainPage.POSSIBILITY_TO_CANCEL_ORDER, *MainPage.ASSERT_POSSIBILITY_TO_CANCEL_ORDER, 'Информация по отмене'],
             [*MainPage.DELIVERY_OUTSIDE_MKAD, *MainPage.ASSERT_DELIVERY_OUTSIDE_MKAD, 'Информация по доставке за мкад'],
             [*MainPage.RETURN_SCOOTER, *MainPage.ASSERT_RETURN_SCOOTER, 'Продлить или вернуть']]

class TestMainPageQuestions:
    @pytest.mark.parametrize('question', questions)
    def test_question_scooter(self, question, browser):
        browser.get("https://qa-scooter.praktikum-services.ru/")
        browser.find_element(By.XPATH, question[1]).send_keys(Keys.ENTER)
        wait_element(browser, By.XPATH, question[3])
        text = browser.find_element(By.XPATH, question[3])
        assert text.is_displayed(), question[4]

    def test_scooter_logo(self, browser):
        browser.get("https://qa-scooter.praktikum-services.ru/")
        click_element(browser, *MainPage.LOGO_SCOOTER)
        order_scooter = browser.find_element(*MainPage.ORDER_PAGE)
        assert order_scooter.is_displayed(), "Найден искомый элемент"

    def test_yandex_logo(self, browser):
        browser.get("https://qa-scooter.praktikum-services.ru/")
        click_element(browser, *MainPage.YANDEX_LOGO)
        assert 'https://dzen.ru/?yredirect=true'