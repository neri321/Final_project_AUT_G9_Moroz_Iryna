import pytest
from uiTesting.pages.page_scroll import PageIntertopScroll


@pytest.mark.smoke
def test_scroll_page(chrome):
    page = PageIntertopScroll(driver=chrome)
    page.open()
    page.scroll_page(5000)
    pass
