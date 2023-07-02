from selenium.webdriver.common.by import By # подключаем пакет для описания локаторов
class CartPage: # описание класса, который будет объектом страницы
    URL = 'http://testshop.sedtest-school.ru/product/17/' # указание страницы авторизации
    IN_CART = (By.CSS_SELECTOR, '#in_cart_link_17') # указание селектора для кнопки добавления в корзину
    MY_CART = (By.CSS_SELECTOR, "a[href='/mycart/']")  # указание селектора для кнопки перехода в корзину
    COUNT = (By.CSS_SELECTOR, "#count_1458")  # указание селектора для изменения количества
    DELETE = (By.CSS_SELECTOR, ".col-md-2 .btn-danger") # указание селектора кнопки удаления
    EMPTY = (By.CSS_SELECTOR, "h1")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)  # открытие страницы
        self.driver.maximize_window()  # максимальный размер окна
        header = self.driver.title  # переменная для проверки заголовка
        assert "TestGym" in header, "Title is {}".format(header)  # проверка заголовка

    def add(self): # функция для добавления товара в корзину
        self.driver.find_element(*self.IN_CART).click()
        self.driver.implicitly_wait(5000)  # ожидание

    def plus(self, number): # функция для увеличения количества товара
        self.driver.find_element(*self.MY_CART).click()
        assert '/mycart' in self.driver.current_url, 'URL is {}".format(self.driver.current_url)'
        self.driver.find_element(*self.COUNT).click()
        self.driver.find_element(*self.COUNT).send_keys(number)
        number = self.driver.find_element(*self.COUNT).text
        assert number in number, "Number is {}".format(number)

    def delete(self): # функция для удаления товара из корзины
        self.driver.find_element(*self.DELETE).click()
        self.driver.implicitly_wait(5000)  # ожидание
        empty = self.driver.find_element(*self.EMPTY).text
        assert "Ваша корзина пуста :(" in empty, "Wrong result"

