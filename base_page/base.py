from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BaseObject:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def is_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def is_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def click_on(self, locator):
        self.is_clickable(locator).click()

    def get_text(self, locator):
        return self.is_visible(locator).text

    def assert_text(self, locator, expected_text):
        actual_text = self.get_text(locator)
        assert actual_text == expected_text, f'Ошибка. Мы ожидали текст: {expected_text}, но получили: {actual_text}'

