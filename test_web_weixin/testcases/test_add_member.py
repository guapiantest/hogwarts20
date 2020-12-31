from test_web_weixin.page.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        # 第一次实例化,实例化首页类
        self.mainPage = MainPage()

    def test_add_member(self):
        # 1.首页->添加成员->添加成员页面->添加成员->回到通讯录首页，获取成员列表
        res = self.mainPage.goto_add_member().add_member().get_member()
        assert "赫敏2" in res

    def test_add_member_by_contact(self):
        pass
