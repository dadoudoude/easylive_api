# -*- coding:utf-8 -*-

import unittest
import requests,urllib3
from ddt import ddt,data,unpack
from common.sendRequests import SendRequests
from common.readExcel import ReadExcel

testData = ReadExcel.readExcel("C:\\Users\\Magic\\PycharmProjects\\easylive_api\\data\\elive_apiTest.xlsx", "Sheet1")
@ddt
class Test1(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()

    def tearDown(self):
        pass

    @data(*testData)
    def test_login_api(self,data):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        re = SendRequests().sendRequests(self.s, data)
        print("re:",re.text)

        #切割字符串取后面的部分
        expect_result1 = str(data["expect_result"])
        #转换为字符串
        expect_result = eval(expect_result1)
        #断言
        self.assertIn(expect_result,re.text)


if __name__ == '__main__':

    unittest.main()