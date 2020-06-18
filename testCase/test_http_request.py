from tools.http_reqest import HttpReqest
import unittest
from tools.do_excel import DoExcel
from ddt import ddt,data
import json
from tools.get_data import GetData
from tools import project_path
import logging


# filename = '../testData/KXliveApiCase.xlsx'
sheel_name = 'community'

#读取excel的数据
test_data = DoExcel().get_data(project_path.case_path)


header = test_data[0]['header']
print('test_data数据类型:',format(type(test_data)))



@ddt
class Test_http_request(unittest.TestCase):

    def setUp(self):
        pass


    @data(*test_data)
    def test_apiRequest(self,item):
        #把URL、接口地址拼接
        url=DoExcel().get_url(project_path.case_path,"init")+item["url"]
        try:

            print("查看替换前的token值：{0}".format(eval(item['header'])['token']))
            # item=eval(item)
            # item['header']['token'] =getattr(GetData,'Token')
            print('Getdata',GetData.Token)
            header = eval(item['header'])
            header['token'] = getattr(GetData, 'Token') #获得token值
            logging.info("替换后的token值：{0}".format(header['token']))
            logging.info("替换token后header的值：{0}".format(header))
            #需要关联时发送的接口请求
            res = HttpReqest().http_reqest(url, eval(item["data"]), header, item["method"])
            logging.info("评论接口返回的结果：{0}".format(res.json()))
        except Exception as e:
            logging.info(e)
            #不需要关联发送的接口请求
            res = HttpReqest().http_reqest(url, eval(item["data"]), eval(item["header"]), item["method"])

        dict_res=res.json()
        logging.info("接口返回内容：{0}".format(dict_res))
        try:
            dict_res["data"]["token"]!=None

            token=dict_res["data"]["token"] #获取返回的token
            logging.info("登录接口返回的token值：{}".format(token))
            setattr(GetData,'Token',token) #用反射保存token值
            token1=getattr(GetData,'Token')
            logging.info("查看登录返回的token是否替换成功：{0}".format(token1))
        except Exception as e:
                logging.info(e)

        code = res.json()["code"]
        result=None

        try:
            self.assertEqual(item["expect"],code)
            result=True

        except:
            result=False
        finally:
            #把返回的结果和用例执行的结果写入excel
            DoExcel().write_data(project_path.case_path, item["sheet_name"], item["id"] + 1, str(res.json()),str(result))

    def tearDown(self):
        pass



if __name__=='__main__':
    unittest.main()