# -*- coding:utf-8 -*-

from common.readExcel import ReadExcel
import requests,urllib3
import json
class SendRequests():
    def sendRequests(self,s,apiData):
        try:
            #从读取的表格中获取响应的参数作为传递
            method = apiData["method"]

            url = apiData["url"]

            if apiData["params"] == "":
                par = None
            else:
                par = eval(apiData["params"])

            if apiData["headers"] == "":
                h = None
            else:
                h = apiData["headers"]


            if apiData["body"] == "":
                body_data = None
            else:
                body_data = eval(apiData["body"])

            type = apiData["type"]

            v = False

            if type == "json":
                body = json.dumps(body_data)
            if type == "data":
                body = body_data
            else:
                body = body_data

            #发送请求
            re = s.request(method=method,url=url,headers=h,params=par,data=body,verify=v)
            return re

        except Exception as e:
            print(e)

if __name__ == '__main__':
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    s = requests.session()
    testData = ReadExcel.readExcel("elive_apiTest.xlsx", "Sheet1")
    response = SendRequests().sendRequests(s,testData[3])
    print(response.json())