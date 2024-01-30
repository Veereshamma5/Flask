import pytest

from HRM_Orange.conftest import *
from HRM_Orange.hrmpages.login_page import LoginPage


@pytest.mark.usefixtures("browser_setup")
class Test_login:

    def setup_class(self):
        self.driver.get(BaseUrl)
        # Creating an obj to the Login_Page
        self.login_page_obj = LoginPage(self.driver)

    def test_valid_login(self):
        self.login_page_obj.login(Username, Password)

    def test_verify_title(self):
        assert "OrangeHRM" == self.login_page_obj.verify_title()

    def test_search_enabled(self):
        self.login_page_obj.search_and_click(SearchText)

    def tear_down(self):
        self.driver.quit()
