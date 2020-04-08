#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest, time
import HTMLTestRunner
from common import *

test_dir = "./testcase"
test_report = "./report"
discover = unittest.defaultTestLoader.discover(test_dir,pattern="*Test.py")#使用discover组织测试用例

if __name__ == '__main__':
    times = time.strftime("%Y%m%d%H%M%S")#格式化当前日期
    report_file = test_report + "/XJtest1.0" + times +"result.html"#组装测试报告路径和文件名
    file = open(report_file, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=file,#方式1：HTML网页的方式实例化测试报告
    #                         title="XJ德迅V1.0接口自动化测试报告",
    #                         description="测试用例执行情况如下")
    runner = unittest.TextTestRunner() #方式2：text文本的执行测试
    runner.run(discover)
    file.close()
    # send_mail(report_file) #发送测试报告