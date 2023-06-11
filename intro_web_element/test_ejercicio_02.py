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
        self.driver.implicitly_wait(2)
        self.driver.get(URL)

    def test_search_tablet(self):
        view_text = "Samsung Galaxy Tab 10.1"
        view_cost = "$241.99"
        view_wishlist = "1"


        link_tablets = self.driver.find_element(By.XPATH, "//a[contains(@href, 'category&path=57')]")
        assert link_tablets.is_displayed() and link_tablets.is_enabled(), "El link de tablets visible y habilitado"
        link_tablets.click()


        action_link = self.driver.find_element(By.XPATH, "//div[@class='caption']//a[contains(@href, 'product_id=49')]")
        assert action_link.is_displayed(), "El menú debe estar visible el click sobre el link"
        assert action_link.text == view_text, f"El título debe ser {view_text}"
        action_link.click()


        tablet_cost = self.driver.find_element(By.XPATH, "//div[@id='content']//li//h2")
        assert tablet_cost.is_displayed(), "El precio de la tablet Samsung Galaxy Tab 10.1 debe ser visible"
        assert tablet_cost.text == view_cost, f"El costo del producto es {view_cost}"

        wishlist_button = self.driver.find_element(By.XPATH, '//div[@id="content"]//button[./i[@class="fa fa-heart"]]')
        assert wishlist_button.is_displayed () and wishlist_button.is_enabled(), "El botón de lista de deseos debe estar habilitado y visible"
        wishlist_button.click()

        wishlist_add = self.driver.find_element(By.XPATH, '//a[@id="wishlist-total"]/span')
        assert wishlist_add.is_displayed(), "La wishlist debe estar visible"
        assert view_wishlist in wishlist_add.text, f"La lista tiene el producto: {view_wishlist}"

        add_carrito = self.driver.find_element(By.ID, "button-cart")
        assert add_carrito.is_displayed() and add_carrito.is_enabled(), "El botón debe estar visible y habilitado"
        add_carrito.click()

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
