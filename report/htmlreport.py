#coding:utf-8
import unittest
import HTMLTestRunner
from report.send_email import main2
def all_case():
    case_dir="C:\\Users\\Magic\\PycharmProjects\\easylive_api\\testcase"
    testcase=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)
    print("dicover",discover)
    testcase.addTests(discover)
    print("testcase:",testcase)
    return testcase
if __name__=="__main__":
    report_path="C:\\Users\\Magic\\PycharmProjects\\easylive_api\\report\\result.html"
    fp=open(report_path,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'易直播API自动化测试报告',description=u'用例执行结果')
    print('start...')
    runner.run(all_case())
    print('ending')
    fp.close()
    print('emailing')
    main2()
    print('end')