import json
import pytest

from apiTesting.pages.page_book_store import PageBookStore


class TestGetBooks:

    @pytest.mark.api
    def test_get_books(self):
        page = PageBookStore()
        status = page.get_books().status_code
        authors = None
        if status == 200:
            content = json.loads(page.get_books().content)
            authors = set([book.get('author') for book in content.get('books')])
            for author in authors:
                print(author)
        assert len(authors) == 8
