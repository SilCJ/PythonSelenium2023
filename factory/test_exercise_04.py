from selenium.webdriver.common.by import By

from factory.webdriver_factory import get_driver

URL = "https://laboratorio.qaminds.com/"


class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)

    def test_search(self):
        search_button = self.driver.__find_clickable_element(By.XPATH, '//*[@class="hidden-xs hidden-sm hidden-md"]')
        search_button.click()

        price_usd = self.driver.__find_visible_element(By.XPATH, '//button[@name="USD"]')
        price_usd.click()

        input_search = self.driver.find_element(By.NAME, "search")
        input_search.send_keys("Samsung")

        search_button = self.driver.__find_clickable_element(By.XPATH, '//*[@class="hidden-xs hidden-sm hidden-md"]')
        search_button.click()

        price_eur = self.driver.__find_clickable_element(By.XPATH, '//button[@name="EUR"]')
        price_eur.click()
        assert cost.is_displayed(), "Cost should be displayed"
        assert price_eur.text < price_usd, f"Cost should be {exp_cost}"

    def __find_clickable_element(self, by: By, value: str):
        return self.element_to_be_clickable((by, value))

    def __find_visible_element(self, by: By, value: str):
        return self.visibility_of_element_located((by, value))

    def __find_by_text(self, by: By, value: str, text: str):
        return self.text_to_be_present_in_element((by, value), text)

    def __wait_until_disappears(self, by: By, value: str):
        self.invisibility_of_element((by, value))

    def teardown_method(self):
        self.driver.quit()