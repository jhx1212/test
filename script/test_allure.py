import allure

class TestLogin:
    def test_a(self):
        print("\n111")
        assert 1

    @allure.step("测试登录步骤")
    def test_b(self):
        print("\n222")
        allure.attach("描述1","请输入用户名")
        print("\n333")
        allure.attach("描述2","请输入密码")
        assert 0
