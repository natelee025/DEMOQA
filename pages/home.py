from base_page.base import BaseObject
from locators.locators import Home as h
from locators.locators import Elements as el


class HomePage(BaseObject):
    def to_elements_page(self):
        self.click_on(h.btn_elements)

    def assert_message(self):
        self.assert_text(el.msg, 'Elements')
