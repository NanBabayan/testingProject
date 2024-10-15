from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from demoQA.lib.drivers import Drivers


class Helpers(Drivers):

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def go_to_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def find_element(self, locator, timeout = 10):
        elem = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        self.scroll_to(elem)
        return elem

    def find_click(self, locator, timeout = 10):
        elem = self.find_element(locator, timeout)
        elem.click()

    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)



