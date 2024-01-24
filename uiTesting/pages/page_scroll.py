from selenium.webdriver.remote.webdriver import WebDriver


class PageIntertopScroll:
    URL = 'https://intertop.ua/uk-ua/shopping/catalog/women/shoes/'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()

    def scroll_page(self, pixels):
        script = f"window.scrollBy(0, {pixels});"
        self.driver.execute_script(script)
