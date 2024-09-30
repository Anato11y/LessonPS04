from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Открываем браузер (Chrome)
browser = webdriver.Chrome()

try:
    # Переход на статью о DOM
    browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
    time.sleep(5)  # Задержка для загрузки страницы

    # Делаем скриншот страницы DOM
    browser.save_screenshot("dom.png")

    # Переход на статью о Selenium на русском
    browser.get("https://ru.wikipedia.org/wiki/Selenium")
    time.sleep(5)

    # Делаем скриншот страницы Selenium
    browser.save_screenshot("selenium.png")

    # Возвращаемся на статью о DOM
    browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
    time.sleep(5)
    browser.save_screenshot("dom_return.png")

    # Переход на статью Selenium повторно
    browser.get("https://ru.wikipedia.org/wiki/Selenium")
    time.sleep(5)
    browser.save_screenshot("selenium_return.png")

    # Обновляем страницу
    browser.refresh()
    time.sleep(5)

    # Переходим на главную страницу русской Википедии
    browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
    assert "Википедия" in browser.title  # Проверяем, что заголовок страницы содержит "Википедия"
    time.sleep(5)

    # Находим поле поиска и вводим запрос "Солнечная система"
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys("Солнечная система")
    search_box.send_keys(Keys.RETURN)  # Нажимаем Enter
    time.sleep(5)

    # Делаем скриншот результатов поиска
    browser.save_screenshot("solar_system_search.png")

finally:
    # Закрываем браузер
    browser.quit()
