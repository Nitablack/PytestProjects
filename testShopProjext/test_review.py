import pytest  # подключаем библиотеку pytest
from selenium import webdriver  # подключаем библиотеку selenium
from pages.review import ReviewPage  # добавляем PageObject

driver = webdriver.Chrome()  # определяем переменную для webdriver
review = ReviewPage(driver)  # определяем переменную для PageObject и делаем объект класса нашей страницы

@pytest.fixture() # определяем фикстуру pre_test,
def pre_test(request): # в которой вызываем функцию
    review.load()        # загрузки страницы нашего PageObject

def teardown_module(module): # делаем фикстуру закрытия браузера,
    driver.close()           # которая будет выполняться после всех тестов

def test_reviewPage(pre_test):
    review.title()
    review.img()
    review.description()
    review.price()
    review.button()
    review.star()
