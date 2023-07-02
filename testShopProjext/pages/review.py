from selenium.webdriver.common.by import By # подключаем пакет для описания локаторов
class ReviewPage: # описываем класс, который будет объектом страницы
    URL = 'http://testshop.sedtest-school.ru/product/17/' # указываем страницу авторизации
    TITLE = (By.CSS_SELECTOR, '.card-title')  # указываем селектор для заголовка товара
    IMAGE = (By.CSS_SELECTOR, ".col-md-6 img")  # указываем селектор картинки товара
    DESCRIPTION = (By.CSS_SELECTOR, ".card-body p")  # указываем селектор описания товара
    PRICE = (By.CSS_SELECTOR, ".card-body .row .col-md-6:nth-child(2) span:nth-child(1)")  # указываем селектор цены
    BUTTON = (By.CSS_SELECTOR, '#in_cart_link_17') # указываем селектор для кнопки добавления в корзину
    STAR = (By.CSS_SELECTOR, '#in_star_link_17')  # указываем селектор для кнопки добавления в избранное

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)  # открытие страницы
        self.driver.maximize_window()  # максимальный размер окна
        header = self.driver.title  # переменная для проверки заголовка
        assert "TestGym" in header, "Title is {}".format(header)  # проверка заголовка

    def title(self): # функция для проверки заголовка товара
        title = self.driver.find_element(*self.TITLE).text  # переменная для проверки заголовка товара
        assert "Google car" in title

    def img(self): # функция для проверки картинки товара
        img = self.driver.find_element(*self.IMAGE)
        assert "/static/products/17.png" in img.get_attribute("src"), "Wrong image"

    def description(self): # функция для проверки описания товара
        description = self.driver.find_element(*self.DESCRIPTION).text
        assert "Совершенно новая машина от гугл с автопилотом!" in description, "Wrong description"

    def price(self): # функция для проверки цены
        price = self.driver.find_element(*self.PRICE).text
        assert "8888888.0 р" in price, "Wrong price"

    def button(self):  # функция для проверки кнопки добавления в корзину
        button = self.driver.find_elements(*self.BUTTON)
        assert len(button) == 1

    def star(self):  # функция для проверки кнопки добавления в избранное
        star = self.driver.find_elements(*self.STAR)
        assert len(star) == 1
