import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/"
class TestLandingPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_search_mobile(self):
        time.sleep(3)

        input_search = self.driver.find_element(By.NAME, "search")
        assert input_search.is_displayed() and input_search.is_enabled(), "El campo de búsqueda tiene que estar visible y habilitado"
        input_search.send_keys("Iphone")


        search_button = self.driver.find_element(By.XPATH, '//div[@id="search"]//button')
        assert search_button.is_displayed(), "El campo debe estar visible"
        assert search_button.is_enabled(), "El campo debe estar habilitado para la captura d ela información"
        search_button.click()

        time.sleep(3)
        iphone_img = self.driver.find_element(By.XPATH, "//img[@alt='iPhone' and contains(@src, 'iphone')]")
        assert iphone_img.is_displayed(), "El nombre de la imagen debe se iphone"
    def teardown_method(self):
        self.driver.quit()







