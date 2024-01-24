import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def chrome():
    driver = webdriver.Chrome()
    driver.implicitly_wait(6)
    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def dyn_prop_page(chrome):
    chrome.get('https://demoqa.com/dynamic-properties')
    yield chrome
