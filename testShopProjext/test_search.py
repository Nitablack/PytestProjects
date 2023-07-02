import pytest  # подключаем библиотеку pytest
from selenium import webdriver  # подключаем библиотеку selenium
from pages.search import SearchPage  # добавляем PageObject wiki

driver = webdriver.Chrome()  # определяем переменную для webdriver
search = SearchPage(driver)  # определяем переменную для PageObject и делаем объект класса нашей страницы

@pytest.fixture() # определяем фикстуру pre_test,
def pre_test(request): # в которой вызываем функцию
    search.load()        # загрузки страницы нашего PageObject

def teardown_module(module): # делаем фикстуру закрытия браузера,
    driver.close()           # которая будет выполняться после всех тестов

def test_search_car(pre_test): # поиск с основной страницы
    search.search('car')

def test_search_apple():  # повторный поиск
    search.search('яблоко')