import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/index.php?route=account/login"
class TestLogin:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_user_invalid(self):
        time.sleep(3)

        field_one = self.driver.find_element(By.XPATH, '//*[@name="email"]')
        assert field_one.is_displayed() and field_one.is_enabled(), "El campo usuario debe estar  visible y habilitado"

        login_user = self.driver.find_element(By.XPATH, '//*[@id="input-email"]')
        assert login_user.is_displayed() and login_user.is_enabled(), "El campo de usuario tiene que estar visible y habilitado"
        login_user.send_keys("jjjjjjjjjjj")

        login_password = self.driver.find_element(By.XPATH, '//*[@id="input-password"]')
        assert login_password.is_displayed() and login_password.is_enabled(), "El campo de password tiene que estar visible y habilitado"
        login_password.send_keys("pppppppppp")

        button_login = self.driver.find_element(By.XPATH, '//*[@value="Login"]')
        assert button_login.is_displayed() and button_login.is_enabled(), "El botón login tiene que estar visible y habilitado"
        button_login.click()
        #assert login_user and login_password.submit(), "Warning: No match for E-Mail Addres and/or Password."
    def teardown_method(self):
            self.driver.quit()