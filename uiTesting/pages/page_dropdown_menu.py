from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PageIntertopDropdown:
    URL = 'https://intertop.ua/uk-ua/shopping/catalog/women/shoes/'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.dropdown_menu_loc = '//span[text()="{}"]'
        self.dropdown_element = '//span[text()="{}"]'
        self.selected_element = '//span[text()="{}"]'
        self.clear_button = '//*[contains(@class, "clear-filter")]'
        self.search_field_dropdown_menu = '//input[@placeholder="{}"]'

    def open(self):
        self.driver.get(self.URL)
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()

    def expand_dropdown_menu(self, value):
        self.driver.find_element(By.XPATH, self.dropdown_menu_loc.format(value)).click()

    def scroll_down_page(self, value):
        target_value = self.driver.find_element(By.XPATH, self.dropdown_element.format(value))
        actions = ActionChains(self.driver)
        actions.move_to_element(target_value).perform()

    def select_element_from_dropdown_menu(self, value):
        self.driver.find_element(By.XPATH, self.dropdown_element.format(value)).click()

    def option_check(self, value):
        result = self.driver.find_element(By.XPATH, self.selected_element.format(value))
        return result.is_displayed()

    def clear_filter(self):
        self.driver.find_element(self.clear_button).click()

    def select_element_via_searching_field(self, name: str, value: str):
        search_field = self.driver.find_element(By.XPATH, self.search_field_dropdown_menu.format(name))
        search_field.click()
        search_field.send_keys(value)
        self.driver.find_element(By.XPATH, self.dropdown_element.format(value)).click()
