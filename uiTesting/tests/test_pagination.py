from time import sleep

import pytest

from uiTesting.pages.page_pagination import PageIntertopPagination


@pytest.mark.usefixtures('chrome')
class TestIntertopPagination:

    @pytest.mark.smoke
    def test_select_more_items_button(self, chrome):
        page = PageIntertopPagination(driver=chrome)
        page.open()
        page.scroll_down_page_to_more_items_button()
        page.select_more_items_button()
        assert page.check_next_page_is_active()
        assert 'page=2' in page.get_current_url()
        sleep(3)

    @pytest.mark.smoke
    def test_qnt_of_img_per_page(self, chrome):
        target_quantity = 48
        page = PageIntertopPagination(driver=chrome)
        page.open()
        page.get_quantity_items_per_page()
        assert target_quantity == page.get_quantity_items_per_page()
