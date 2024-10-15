from selenium import webdriver

class Drivers:

    @staticmethod
    def get_driver_by_name(driver_name = "chrome"):
        if driver_name == "chrome":
            return webdriver.Chrome()
        elif driver_name == "edge":
            return  webdriver.ChromiumEdge()
        elif driver_name == "firefox":
            return webdriver.Firefox()
        else:
            print("The driver is missing!")