from selenium.webdriver.common.by import By

from factory.webdriver_factory import get_driver

URL = "https://laboratorio.qaminds.com/"
class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)
    def test_slow_loading_page(self):
        input_search = self.driver.find_element(By.NAME, "search")
        assert input_search.is_displayed() and input_search.is_enabled(), "El campo de búsqueda tiene que estar visible y habilitado"
        input_search.send_keys("Iphone")

    def teardown_method(self):
            self.driver.quit()