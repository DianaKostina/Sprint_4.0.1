from selenium.webdriver.common.by import By


class LocatorOrderYaScooterPage:
    YANDEX_BUTTON = (By.XPATH, "//img[@alt='Yandex']")
    SCOOTER_BUTTON = (By.XPATH, "//img[@alt='Scooter']")
    FIRST_NAME = (By.XPATH, "//input[contains(@placeholder, '* Имя')]")
    LAST_NAME = (By.XPATH, "//input[contains(@placeholder, '* Фамилия')]")
    ADDRESS = (By.XPATH, "//input[contains(@placeholder, '* Адрес: куда привезти заказ')]")
    STATION = (By.XPATH, "//input[contains(@placeholder, '* Станция метро')]")
    PHONE_NUMBER = (By.XPATH, "//input[contains(@placeholder, '* Телефон: на него позвонит курьер')]")
    BUTTON_NEXT = (By.XPATH, "//button[contains(text(),'Далее')]")
    DELIVERY_DATE = (By.XPATH, "//input[contains(@placeholder, '* Когда привезти самокат')]")
    RENTAL_PERIOD = (By.XPATH, "//div[contains(text(),'* Срок аренды')]")
    RENTAL_PERIOD_VALUE_1 = (By.XPATH, "//div[contains(text(),'сутки')]")
    RENTAL_PERIOD_VALUE_2 = (By.XPATH, "//div[contains(text(),'двое суток')]")
    SCOOTER_BLACK_COLOR_CHECKBOX = (By.ID, "black")
    SCOOTER_GREY_COLOR_CHECKBOX = (By.ID, "grey")
    COMMENT = (By.XPATH, "//input[contains(@placeholder, 'Комментарий для курьера')]")
    BUTTON_ORDER_MIDDLE = (By.XPATH, "//button[contains(@class,'Button_Middle') and contains(text(),'Заказать')]")
    BUTTON_ORDER_YES = (By.XPATH, "//button[contains(text(),'Да')]")
    SUCCESSFUL_ORDER = (By.XPATH, "//div[contains(@class,'Order_ModalHeader')]")
