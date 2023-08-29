from selenium.webdriver.common.by import By
class MainPage:
    #1
    SCOOTER_PRICE = (By.XPATH, "//div[@id='accordion__heading-0']")
    ASSERT_SCOOTER_PRICE = (By.XPATH, "//p[contains(text(),'Сутки — 400 рублей. Оплата курьеру — наличными или')]")

    #2
    SEVERAL_SCOOTER = (By.XPATH, "//div[@id='accordion__heading-1']")
    ASSERT_SEVERAL_SCOOTER = (By.XPATH, "//p[contains(text(),'Пока что у нас так: один заказ — один самокат. Есл')]")
    #3
    RENTAL_TIME = (By.XPATH, "//div[@id='accordion__heading-2']")
    ASSERT_RENTAL_TIME = (By.XPATH, "//p[contains(text(),'Допустим, вы оформляете заказ на 8 мая. Мы привози')]")
    #4
    ORDER_A_SCOOTER_TODAY = (By.XPATH, "//div[@id='accordion__heading-3']")
    ASSERT_ORDER_A_SCOOTER_TODAY = (By.XPATH, "//p[contains(text(),'Только начиная с завтрашнего дня. Но скоро станем ')]")

    #5
    RETURN_SCOOTER = (By.XPATH, "//*[contains(text(),'Можно ли продлить заказ или вернуть самокат раньше?')]")
    ASSERT_RETURN_SCOOTER = (By.XPATH, "//p[contains(text(),'Пока что нет! Но если что-то срочное — всегда можн')]")

    #6
    CHARGING_IS_PROVIDED = (By.XPATH, "//div[@id='accordion__heading-5']")
    ASSERT_CHARGING_IS_PROVIDED = (By.XPATH, "//p[contains(text(),'Самокат приезжает к вам с полной зарядкой. Этого х')]")

    #7
    POSSIBILITY_TO_CANCEL_ORDER = (By.XPATH, "//div[@id='accordion__heading-6']")
    ASSERT_POSSIBILITY_TO_CANCEL_ORDER = (By.XPATH, "//p[contains(text(),'Да, пока самокат не привезли. Штрафа не будет, объ')]")
    #8
    DELIVERY_OUTSIDE_MKAD = (By.XPATH, "//div[@id='accordion__heading-7']")
    ASSERT_DELIVERY_OUTSIDE_MKAD = (By.XPATH, "//p[contains(text(),'Да, обязательно. Всем самокатов! И Москве, и Моско')]")
    LOGO_SCOOTER = (By.XPATH, "//img[@src='/assets/scooter.svg']")
    ORDER_PAGE = (By.XPATH, "//div[contains(text(), 'Заказываете самокат')]")
    YANDEX_LOGO = (By.XPATH, "//img[@src='/assets/ya.svg']")
    ORDER_DOWN = (By.XPATH, "//*[contains(@class, 'FinishButton')]//button[contains(text(), 'Заказать')]")
    ORDER_HIGH = (By.XPATH, "//*[contains(@class, 'Header_Nav')]//button[contains(text(), 'Заказать')]")

class Order:
    WANT_TO_ORDER = (By.XPATH, "//button[contains(text(),'Да')]")
    WANT_TO_CANCEL_AN_ORDER = (By.XPATH, "//button[contains(text(),'Нет')]")
    VIEW_ORDER_STATUS = (By.XPATH, "//button[contains(text(),'Посмотреть статус')]")
    ST = (By.XPATH,  "//*[contains(text(),'Бульвар Рок')]")
    ORDER = (By.XPATH, "//*[contains(@class, 'Order_Buttons')]//button[contains(text(), 'Заказать')]")
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    NUMBER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    IMPORT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATA_SELECTION = (By. XPATH, "//div[@class='react-datepicker__week']//*[contains(text(),'28')]")
    RENT_DEADLINE = (By.XPATH, "//div[@class ='Dropdown-placeholder']")
    DAY = (By.XPATH, "//div[contains(text(),'двое суток')]")
    COMMENTS = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    NEXT = (By.XPATH, "//button[contains(text(), 'Далее')]")
    BLACK_STONE = (By.XPATH, "//label[contains(text(),'чёрный жемчуг')]")
    GREY = (By.XPATH, "//label[contains(text(),'серая безысходность')]")
    COMING_TO_YOU = (By.XPATH, "//div[contains(text(),'едет к вам')]")
    ORDER_DOWN = (By.XPATH, "//*[contains(@class, 'FinishButton')]//button[contains(text(), 'Заказать')]")
    ORDER_HIGH = (By.XPATH, "//*[contains(@class, 'Header_Nav')]//button[contains(text(), 'Заказать')]")
    LOGO_SCOOTER = (By.XPATH, "//img[@src='/assets/scooter.svg']")