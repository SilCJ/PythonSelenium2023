
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html"


class TestLandingPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.implicitly_wait(10)
        self.wait_driver = WebDriverWait(self.driver, 120)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_slow_loading_page(self):
        # Obtener el elemento, y el estado importa
        button = self.__find_clickable_element(By.ID, "downloadButton")
        button.click()
        label = self.__find_by_text(By.CLASS_NAME, "progress-label", "Complete!")

        label_dos = self.__find_visible_element(By.CLASS_NAME, "ui-dialog-titlebar-close")

    def __find_clickable_element(self, by: By, value: str):
        return self.wait_driver.until(EC.element_to_be_clickable((by, value)))

    def __find_visible_element(self, by: By, value: str):
        return self.wait_driver.until(EC.visibility_of_element_located((by, value)))

    def __find_by_text(self, by: By, value: str, text: str):
        return self.wait_driver.until(EC.text_to_be_present_in_element((by, value), text))

    def __wait_until_disappears(self, by: By, value: str):
        self.wait_driver.until(EC.invisibility_of_element((by, value)))

    def teardown_method(self):
        self.driver.quit()