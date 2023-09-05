import pytest
from data import Data
from urls import Urls
from locators.yandex_browser_main_page import LocatorYandexBrowserMainPage
from pages.ya_scooter_main_page import YaScooterMainPage
from locators.ya_scooter_main_page_locators import LocatorMainYaScooterPage


class TestCheckAccordion():

    @pytest.mark.parametrize('question,answer,answer_on_question',
                             [
                                 [LocatorMainYaScooterPage.QUESTION_ONE, LocatorMainYaScooterPage.ANSWER_ONE, Data.answers_on_questions[0]],
                                 [LocatorMainYaScooterPage.QUESTION_TWO, LocatorMainYaScooterPage.ANSWER_TWO, Data.answers_on_questions[1]],
                                 [LocatorMainYaScooterPage.QUESTION_THRE, LocatorMainYaScooterPage.ANSWER_THREE, Data.answers_on_questions[2]],
                                 [LocatorMainYaScooterPage.QUESTION_FOUR, LocatorMainYaScooterPage.ANSWER_FOUR, Data.answers_on_questions[3]],
                                 [LocatorMainYaScooterPage.QUESTION_FIVE, LocatorMainYaScooterPage.ANSWER_FIVE, Data.answers_on_questions[4]],
                                 [LocatorMainYaScooterPage.QUESTION_SIX, LocatorMainYaScooterPage.ANSWER_SIX, Data.answers_on_questions[5]],
                                 [LocatorMainYaScooterPage.QUESTION_SEVEN, LocatorMainYaScooterPage.ANSWER_SEVEN, Data.answers_on_questions[6]],
                                 [LocatorMainYaScooterPage.QUESTION_EIGHT, LocatorMainYaScooterPage.ANSWER_EIGHT, Data.answers_on_questions[7]]
                             ])
    def test_check_answer(self, driver, question, answer, answer_on_question):
        ya_scooter_main_page = YaScooterMainPage(driver)
        ya_scooter_main_page.go_to_site(Urls.url_main_page)
        ya_scooter_main_page.enter_on_button(question)
        ya_scooter_main_page.find_element(answer)
        assert ya_scooter_main_page.get_text(answer) == answer_on_question

    def test_go_to_yandex_page(self, driver):
        ya_scooter_main_page = YaScooterMainPage(driver)
        ya_scooter_main_page.go_to_site(Urls.url_main_page)
        ya_scooter_main_page.click_on_button_main_page()
        driver.switch_to.window(driver.window_handles[1])
        ya_scooter_main_page.find_element(LocatorYandexBrowserMainPage.NAVIGATION_BAR)
        assert ya_scooter_main_page.get_text_main_page() == "Новости"


