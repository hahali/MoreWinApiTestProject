import unittest
import BSTestRunner
import logging
import time
from testCase.test_http_request import Test_http_request
from tools import project_path
# def run(test_data,sheet_name):
#
#     for item in test_data:
#         #调用方法http_reqest()发起request请求
#         res=HttpReqest().http_reqest(item["url"],eval(item["data"]),eval(item["header"]),item["method"])
#         print(res.json())
#         DoExcel().write_data(filename,sheet_name,item["id"]+1,str(res.json()))

# #工作薄路径
# filename='../testData/KXliveApiCase.xlsx'
# #调用get_data方法获取excel测试数据
# test_data=DoExcel().get_data(filename,'login')
# #调用run函数发起接口请求
# run(test_data,'login')


#discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_http_request.py') #加载测试目录下的所有测试文件

#时间格式化
now=time.strftime('%Y-%m-%d %H_%M_%S')
report_name=project_path.report_dir+'/'+now+' test_report.html'#测试报告

suite=unittest.TestSuite()
loader=unittest.TestLoader()
testCase=loader.loadTestsFromTestCase(Test_http_request)#返回测试类中的所有测试用例
suite.addTest(testCase) #把测试用例加入测试套件
#suite.addTest()


if __name__=='__main__':
    with open(report_name,'wb') as f:
        runner = BSTestRunner.BSTestRunner(stream=f, title='KXlive_API_测试报告', description='登录模块测试报告')
        #runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='KXlive_API_测试报告', description='登录模块测试报告')
        logging.info('start run test case...')
        #runner.run(discover)
        runner.run(suite)
