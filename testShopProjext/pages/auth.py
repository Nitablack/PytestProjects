from selenium.webdriver.common.by import By # подключаем пакет для описания локаторов
class AuthPage: # описываем класс, который будет объектом страницы
    URL = "http://testshop.sedtest-school.ru/users/auth/" # указываем страницу авторизации
    INPUT_BUTTON = (By.CLASS_NAME, "btn-info") # указываем кнопку входа
    OUTPUT_BUTTON = (By.CLASS_NAME, "btn-danger") # указываем кнопку выхода
    EMAIL = (By.CSS_SELECTOR, "#id_email") # указываем инпут почты
    PASSWORD = (By.CSS_SELECTOR, "#id_password") # указываем инпут пароля

    def __init__(self, driver):
        self.driver = driver

    def load(self):  # функция загрузки страницы авторизации
        self.driver.get(self.URL)   # открытие страницы
        self.driver.maximize_window()  # максимальный размер окна
        header = self.driver.title  # переменная для проверки заголовка
        assert "Авторизация" in header, "Title is {}".format(header)  # проверка заголовка

    def check(self):   # функция проверки авторизации
        self.driver.implicitly_wait(5000)   # ожидание
        header = self.driver.find_element(*self.OUTPUT_BUTTON).text  # переменная для проверки заголовка
        assert "Выйти" in header, "test failed"  # проверка заголовка

    def auth(self, email, password): # функция авторизации
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.INPUT_BUTTON).click()