import pytest

from uiTesting.pages.page_dropdown_menu import PageIntertopDropdown


@pytest.mark.usefixtures('chrome')
class TestIntertopDropDown:

    def test_dropdown_menu(self, chrome):
        name = "Бренд"
        selected_value = "Marc O’Polo"
        page = PageIntertopDropdown(driver=chrome)
        page.open()
        page.expand_dropdown_menu(name)
        page.scroll_down_page(selected_value)
        page.select_element_from_dropdown_menu(selected_value)
        assert page.option_check(selected_value)

    @pytest.mark.skip
    def test_clear_filters(self, chrome):
        page = PageIntertopDropdown(driver=chrome)
        page.open()
        page.clear_filter()
        pass

    def test_search_field_dropdown_menu(self, chrome):
        name = "Бренд"
        field_placeholder_name = "Знайти бренд"
        selected_value = "Marc O’Polo"
        page = PageIntertopDropdown(driver=chrome)
        page.open()
        page.expand_dropdown_menu(name)
        page.select_element_via_searching_field(field_placeholder_name, selected_value)
        assert page.option_check(selected_value)
