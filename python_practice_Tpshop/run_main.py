"""
    运行程序
"""
# 导包
import unittest
import time

from tool.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestLoader().discover(r"./scripts")
dir_path = r"./report/{}.html".format(time.strftime("%Y_%m_%d_%H_%M_%S"))
with open(dir_path, "wb") as f:
    HTMLTestRunner(stream=f, title="Tpshop商城自动化测试报告").run(suite)