from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose Language, using --language [var]")


@pytest.fixture(scope="session")
def driver(request):
    options = Options()

    language = request.config.getoption("language")
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()
