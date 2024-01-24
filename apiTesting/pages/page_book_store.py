import requests


class PageBookStore:
    URL = 'https://demoqa.com'

    def __init__(self):
        self.books = requests.get(self.URL + '/BookStore/v1/Books')

    def get_books(self):
        return self.books
