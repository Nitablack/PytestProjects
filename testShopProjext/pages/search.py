from selenium.webdriver.common.by import By # подключаем пакет для описания локаторов
class SearchPage: # описываем класс, который будет объектом страницы
    URL = 'http://testshop.sedtest-school.ru/' # указываем страницу авторизации
    #TITLE = (By.ID, 'mp-welcome')
    SEARCH_INPUT = (By.CSS_SELECTOR, '.form-group [name="search"]')
    CARD_BODY = (By.CSS_SELECTOR, 'h5>.text-info')
    #HEADER = (By.CSS_SELECTOR, "#firstHeading")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)  # открытие страницы
        self.driver.maximize_window()  # максимальный размер окна
        header = self.driver.title  # переменная для проверки заголовка
        assert "TestGym" in header, "Title is {}".format(header)  # проверка заголовка

    def search(self, word): # функция поиска
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(word)
        self.driver.find_element(*self.SEARCH_INPUT).send_keys('\ue007')
        self.driver.implicitly_wait(5000)
        card = self.driver.find_element(*self.CARD_BODY).text  # переменная для проверки поиска
        assert word in card, "test failed"  # проверка результата поиска