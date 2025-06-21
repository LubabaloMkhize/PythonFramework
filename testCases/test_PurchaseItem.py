import pytest

from utilities.readProperties import ReadConfig


class Test_001_PurchaseItem:
    baseURL=ReadConfig.getBaseURL()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_purchaseItems(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)



