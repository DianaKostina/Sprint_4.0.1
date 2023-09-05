from locators.ya_scooter_main_page_locators import LocatorMainYaScooterPage
from locators.ya_scooter_order_page_locators import LocatorOrderYaScooterPage
from pages.ya_scooter_order_page import YaScooterOrderPage
from urls import Urls


class TestCreateOrder():

    def test_order_one_button(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.url_main_page)
        ya_scooter_order_page.fill_field_for_order_via_top_button()
        assert "Заказ оформлен" in ya_scooter_order_page.get_text_successful_order()

    def test_order_two_button(self, driver):
        scooter_order_page = YaScooterOrderPage(driver)
        scooter_order_page.go_to_site(Urls.url_main_page)
        scooter_order_page.fill_field_for_order_via_middle_button()
        assert "Заказ оформлен" in scooter_order_page.get_text_successful_order()

    def test_scooter_button(self, driver):
        scooter_order_page = YaScooterOrderPage(driver)
        scooter_order_page.go_to_site(Urls.url_main_page)
        scooter_order_page.enter_on_button_order_in_header()
        scooter_order_page.click_on_button_scooter()
        assert scooter_order_page.get_text_block_with_questions() == "Вопросы о важном"