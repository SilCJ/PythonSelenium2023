import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = " https://demoqa.com/select-menu"


class TestLandingPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(URL)

    def test_cars_select(self):
        element = self.driver.find_element(By.ID, "cars")
        select = Select(element)
        select.select_by_value("saab")
        select.select_by_value("opel")
        select.select_by_visible_text("Audi")
        assert select.first_selected_option.text == "Saab"
        select.deselect_all()
        select.select_by_value("volvo")
        select.select_by_visible_text("Audi")
        select.all_selected_options

        all_selections = select.all_selected_options
        for option in all_selections:
            print (f"Las opciones seleccionadas son {option.text}")


    def teardown_method(self):
        self.driver.quit()