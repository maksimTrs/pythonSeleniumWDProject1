import pytest

from pages.HomePage import HomePage
from testdata.home_page_data import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is " + getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        homepage.set_birth_data(getData["birthday"])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        # self.driver.refresh()

    # @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param
