from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class IntertopPageSearch:
    URL = 'https://intertop.ua/uk-ua/shopping/catalog/women/shoes/'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.search_input = (By.ID, "v_search_input")
        self.search_button = (By.CLASS_NAME, "btn-search")

    def open(self):
        self.driver.get(self.URL)
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()

    def enter_search_query(self, query):
        search_box = self.driver.find_element(*self.search_input)
        search_box.send_keys(query)

    def click_search_button(self):
        search_button = self.driver.find_element(*self.search_button)
        search_button.click()
