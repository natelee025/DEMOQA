import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service as chrome_service
from webdriver_manager.chrome import ChromeDriverManager
from pages.home import HomePage
from pages.elements import ElementsPage

from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.firefox.service import Service as firefox_service
from webdriver_manager.firefox import GeckoDriverManager


# Chrome

@pytest.fixture()
def get_chrome_options():
    options = chrome_options()
    options.add_argument('--start-maximized')
    return options


@pytest.fixture()
def get_chrome_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options, service=chrome_service(ChromeDriverManager().install()))
    return driver


@pytest.fixture()
def setup_chrome(get_chrome_webdriver):
    driver = get_chrome_webdriver
    url = 'https://demoqa.com/'
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture()
def setup_chrome_elements(get_chrome_webdriver):
    driver = get_chrome_webdriver
    url = 'https://demoqa.com/'
    driver.get(url)
    HomePage(driver).to_elements_page()
    yield driver
    driver.quit()


@pytest.fixture()
def home_ch(setup_chrome):
    return HomePage(setup_chrome)


@pytest.fixture()
def elements_ch(setup_chrome_elements):
    return ElementsPage(setup_chrome_elements)


# Firefox

@pytest.fixture()
def get_firefox_options():
    options = firefox_options()
    options.add_argument('--start-maximized')
    options.accept_untrusted_certs = True
    return options


@pytest.fixture()
def get_firefox_webdriver(get_firefox_options):
    options = get_firefox_options
    driver = webdriver.Firefox(options=options, service=firefox_service(GeckoDriverManager().install()))
    return driver


@pytest.fixture()
def setup_firefox(get_firefox_webdriver):
    driver = get_firefox_webdriver
    url = 'https://demoqa.com/'
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture()
def setup_firefox_elements(get_firefox_webdriver):
    driver = get_firefox_webdriver
    url = 'https://demoqa.com/'
    driver.get(url)
    HomePage(driver).to_elements_page()
    yield driver
    driver.quit()


@pytest.fixture()
def home_fx(setup_firefox):
    return HomePage(setup_firefox)


@pytest.fixture()
def elements_fx(setup_firefox_elements):
    return ElementsPage(setup_firefox_elements)
