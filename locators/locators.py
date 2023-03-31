from selenium.webdriver.common.by import By


class Home:
    btn_elements = (By.CSS_SELECTOR, '.category-cards > div:first-child')

class Elements:
    msg = (By.CLASS_NAME, 'main-header')
    btn_check_box = (By.ID, 'item-1')
    dir_home = (By.CSS_SELECTOR, '#tree-node > ol > li > span .rct-collapse.rct-collapse-btn')
    dir_download = (By.CSS_SELECTOR, '#tree-node > ol li:nth-child(3) .rct-collapse.rct-collapse-btn')
    word_file = (By.CSS_SELECTOR, 'label[for=tree-node-wordFile]')
    result_msg = (By.ID, 'result')
