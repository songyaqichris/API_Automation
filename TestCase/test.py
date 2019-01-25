import allure


@allure.MASTER_HELPER.feature("测试Dome")
class TestDome(object):

    @allure.MASTER_HELPER.step("定义被测函数")
    def func(self, x):
        return x+1

    @allure.MASTER_HELPER.story("被测场景")
    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.step("断言结果")
    def test_func(self):
        # with allure.MASTER_HELPER.step("断言结果"):
        allure.MASTER_HELPER.attach("预期结果", "{}".format(self.func(3)))
        allure.MASTER_HELPER.attach("实际结果", "{}".format(5))
        assert self.func(3) == 5
