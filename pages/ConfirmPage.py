from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country_field = (By.ID, "country")
    country_name = (By.LINK_TEXT, "India")
    confirm_checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase_btn = (By.CSS_SELECTOR, "[type='submit']")
    purchase_result = (By.CSS_SELECTOR, "[class*='alert-success']")

    def set_country_field(self, country):
        self.driver.find_element(*ConfirmPage.country_field).send_keys(country)

    def get_country_name(self):
        self.driver.find_element(*ConfirmPage.country_name).click()

    def submit_purchase_with_checkbox(self):
        self.driver.find_element(*ConfirmPage.confirm_checkbox).click()
        self.driver.find_element(*ConfirmPage.purchase_btn).click()

    def get_purchase_result(self):
        return self.driver.find_element(*ConfirmPage.purchase_result).text

