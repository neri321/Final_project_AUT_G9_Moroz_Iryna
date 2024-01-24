import pytest
from uiTesting.pages.page_search import IntertopPageSearch


@pytest.mark.smoke
def test_search_on_intertop(chrome):
    search_query = "Marc O’Polo"
    page = IntertopPageSearch(driver=chrome)
    page.open()
    page.enter_search_query(search_query)
    page.click_search_button()
    assert search_query in chrome.page_source
