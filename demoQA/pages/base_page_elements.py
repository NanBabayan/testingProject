from selenium.webdriver.common.by import By

from demoQA.lib.helpers import Helpers


class BasePage(Helpers):

    menu_items = {
        "element_menu_item": (By.XPATH, '(//*[@class = "card-up"])[1]'),
        "form_menu_item": (By.XPATH, '(//*[@class = "card-up"])[2]'),
        "alert_frame_window_menu_item": (By.XPATH, '(//*[@class = "card-up"])[3]'),
        "widgets_menu_item": (By.XPATH, '(//*[@class = "card-up"])[4]'),
        "interactions_menu_item": (By.XPATH, '(//*[@class = "card-up"])[5]'),
        "book_store_menu_item": (By.XPATH, '(//*[@class = "card-up"])[6]'),
    }

    def click_on_menu_item(self, item_name):
        if item_name in self.menu_items:
            locator = self.menu_items[item_name]
            self.find_click(locator)
        else:
            print(f"Menu item '{item_name}' not found in the menu_items dictionary.")
