from demoQA.lib.assertions import Assertion
from demoQA.lib.drivers import Drivers
from demoQA.lib.helpers import Helpers
from demoQA.pages.base_page_elements import BasePage
from demoQA.testData.base_page_data import BasePageData


class MenuElementTest:

    def __init__(self):
        self.driver = Drivers.get_driver_by_name()
        self.helper = Helpers(self.driver)
        self.basePage = BasePage(self.driver)
        self.assertion = Assertion()


    def menu_elem_test(self, menu_item, expected_url):
        self.helper.go_to_page(BasePageData.base_url)
        self.basePage.click_on_menu_item(menu_item)
        actual_url = self.driver.current_url
        assert self.assertion.assert_that(actual_url, expected_url), \
            f"Expected URL: {expected_url}, but got {actual_url}"


menu_element_test = MenuElementTest()
menu_element_test.menu_elem_test("element_menu_item", "https://demoqa.com/elements")
menu_element_test.menu_elem_test("form_menu_item", "https://demoqa.com/forms")
menu_element_test.menu_elem_test("alert_frame_window_menu_item", "https://demoqa.com/alertsWindows")
menu_element_test.menu_elem_test("widgets_menu_item", "https://demoqa.com/widgets")
menu_element_test.menu_elem_test("interactions_menu_item", "https://demoqa.com/interaction")
menu_element_test.menu_elem_test("book_store_menu_item", "https://demoqa.com/books")
