from locators.locators import Elements as el
from base_page.base import BaseObject


class ElementsPage(BaseObject):
    def to_check_box(self):
        self.click_on(el.btn_check_box)

    def open_dir_home(self):
        self.click_on(el.dir_home)

    def open_dir_downloads(self):
        self.click_on(el.dir_download)

    def select_word_file(self):
        self.click_on(el.word_file)

    def assert_selected_file(self):
        self.assert_text(el.result_msg, 'You have selected :\nwordFile')
