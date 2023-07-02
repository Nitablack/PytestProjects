import pytest  # подключение библиотеки pytest
from selenium import webdriver  # подключение библиотеку selenium
from pages.cart import CartPage  # добавление PageObject

driver = webdriver.Chrome()  # определение переменной для webdriver
cart = CartPage(driver)  # определение переменной для PageObject и создание объекта класса страницы

@pytest.fixture() # определение фикстуры pre_test,
def pre_test(request): # в которой вызывается функция
    cart.load()        # загрузки страницы PageObject

def teardown_module(module): # создание фикстуры закрытия браузера,
    driver.close()           # которая будет выполняться после всех тестов

def test_cartPage(pre_test): # создание функции теста корзины
    cart.add() # добавление товара в корзину
    cart.plus(5) # изменение количества товара
    cart.delete() # удаление товара из корзины
