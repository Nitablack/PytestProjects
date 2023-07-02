import pytest  # подключаем библиотеку pytest
from selenium import webdriver  # подключаем библиотеку selenium
from pages.auth import AuthPage  # добавляем PageObject wiki

driver = webdriver.Chrome()  # определяем переменную для webdriver
auth = AuthPage(driver)  # определяем переменную для PageObject и делаем объект класса нашей страницы

@pytest.fixture() # определяем фикстуру pre_test,
def pre_test(request): # в которой вызываем функцию
    auth.load()        # загрузки страницы нашего PageObject

def teardown_module(module): # делаем фикстуру закрытия браузера,
    driver.close()           # которая будет выполняться после всех тестов

def test_auth(pre_test): # функция авторизации
    auth.auth("cruella@devill.hell", "123456Aa")
    auth.check()
