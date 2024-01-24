from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class PageIntertopPagination:
    URL = 'https://intertop.ua/uk-ua/shopping/catalog/women/shoes/'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.more_items_button = '//div[contains(@class, "sprite-svg")]'
        self.image_locator = '//img[contains(@loading, "lazy")]'
        self.page_two_button = '//a[contains(text(),"2")]'

    def open(self):
        self.driver.get(self.URL)
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()

    def get_current_url(self):
        return self.driver.current_url

    def scroll_down_page_to_more_items_button(self):
        pag_menu = self.driver.find_element(By.XPATH, self.more_items_button)
        actions = ActionChains(self.driver)
        actions.move_to_element(pag_menu).perform()

    def select_more_items_button(self):
        self.driver.find_element(By.XPATH, self.more_items_button).click()

    def get_quantity_items_per_page(self) -> int:
        qnt_items_per_page = self.driver.find_elements(By.XPATH, self.image_locator)
        return len(qnt_items_per_page)

    def check_next_page_is_active(self):
        try:
            WebDriverWait(self.driver, 10).until(
                ec.text_to_be_present_in_element_attribute((By.XPATH, self.page_two_button),
                                                           attribute_='class', text_='active'))
            print('The next page is loaded successfully!')
            return True
        except TimeoutException:
            print("Loading took too much time!")
            raise False
