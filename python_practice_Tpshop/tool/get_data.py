"""
    读取测试用例数据
"""
# 登录测试数据文件名
login_data = "login_data.txt"
# 注册测试数据文件名
register_data = "register_data.txt"

class GetData:
    # 读取数据
    def read_data(self, data_name):
        data_list = []
        path = r"../data/" + data_name
        # 打开数据问件
        with open(path, mode="r", encoding="utf_8") as f:
            # 读取数据
            return_data = f.readlines()
        # 遍历返回数据
        for data in return_data:
            data = data.strip().split(",")
            data_list.append(data)
        # 返回测试用例数据
        return data_list[1 :]

    # 获得登录测试用例数据
    def data_login(self):
        return self.read_data(login_data)

    # 获得注册测试用例数据
    def data_register(self):
        return self.read_data(register_data)