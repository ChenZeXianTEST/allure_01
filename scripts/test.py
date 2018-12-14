import allure
import pytest


class Test:

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="测试步骤01")
    def test01(self):
        allure.attach("描述:", "增")
        print("增")

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="测试步骤02")
    def test02(self):
        allure.attach("描述:", "改")
        print("改")

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="测试步骤03")
    def test03(self):
        allure.attach("描述:", "查")
        print("查")

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="测试步骤04")
    def test04(self):
        allure.attach("描述:", "删")
        print("删")