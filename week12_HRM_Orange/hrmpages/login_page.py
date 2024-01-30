from selenium.webdriver.common.by import By

from HRM_Orange.hrmhelper.selenium_helper import Selenium_Helper


class LoginPage(Selenium_Helper):
    email_ele = (By.XPATH, "//input[@placeholder='Username']")
    password_ele = (By.XPATH, "//input[@placeholder='Password']")
    login_ele = (By.XPATH, "//button[@type='submit']")
    search_button = (By.XPATH, "// input[ @ placeholder = 'Search']")
    admin_link = (By.XPATH, "//a[@class='oxd-main-menu-item']")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        Selenium_Helper.webelement_enter(self, self.email_ele, username)
        Selenium_Helper.webelement_enter(self, self.password_ele, password)
        Selenium_Helper.webelement_click(self, self.login_ele)

    def verify_title(self):
        hrm_tilte = Selenium_Helper.webelement_gettile(self)
        return hrm_tilte

    def search_and_click(self, text):
        Selenium_Helper.webelement_enter(self, self.search_button, text)
        Selenium_Helper.webelement_click(self, self.admin_link)


