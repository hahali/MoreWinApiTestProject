import requests
import logging

class HttpReqest:
    def http_reqest(self,url,data,header,http_method):
        try:
            if http_method.upper()=="GET":
                res=requests.get(url,data,header)
            elif http_method.upper()=="POST":
                res=requests.post(url,json=data,headers=header)
            else:
                print("输入请求方法")
        except Exception as e:
            print("请求报错了:{0}".format(e))
            raise
        return res

if __name__=="__main__":
    login_url = 'http://kxlive-node-api.nn722.com/user/login'
    login_data = {"phone": "18927509566",
                  "password": "123456",
                  "platform": "kxlive",
                  "terminal": "pc",
                  "expire": 10000,
                  "ip": "183.63.114.61",
                  "clientId": "abc"}
    login_head = {"Content-Type": "application/json"}
    login_res=HttpReqest().http_reqest(login_url,login_data,login_head,"post")
    logging.info(login_res.json())
    # login_res = requests.post(url=login_url, json=login_data, headers=login_head)