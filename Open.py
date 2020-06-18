# coding:utf-8
import requests
import time
import datetime
import hashlib
from Crypto.Cipher import AES
import  base64
import json
from Crypto.Util.Padding import pad, unpad
class OpenTest():
    def ChongZhi(self):
        #EncryptKey = "KgRP3T9fezwGY769"
        AppKey = "2d2fb421-e2e0-47cd-b88c-573982f83abb"
        appId=1000
        langCode="en-US"
        # 获取时间戳
        t = int(time.time())
        #print(t)
        data_chong = {"userId": "mw@198"}
        #加密参数
        data_chong = json.dumps(data_chong)
        print('param加密前为：' + data_chong)
        param=self.encrypt_ecb(data_chong)

        param = param.replace("\n","")
        print('param加密后为：' + param)
        # param="/t+xYFvu21uTTTq9I5n2sFU3NiLzNf645H5su0yIkLo="
        #python使用MD5加密
        str_param=str(appId)+str(param)+str(t)+str(langCode)+str(AppKey)
        # str='this is a md5 test'
        m = hashlib.md5()
        b = str_param.encode(encoding='utf-8')
        m.update(b)
        str_md5 = m.hexdigest()
        print('MD5加密前为:' + str_param)
        print('MD5加密后为:' + str_md5)
        #拉取用户数据接口
        url = "http://mwsys-open-api.nn722.com/open_api/account/getUserInfo"
        data = {
                "appId": 1000,
                "sign": str_md5,
                "param": param,
                "timestamp": t,
                "langCode": "en-US",
                }
        headers={
            "Content-Type":"application/json"
        }
        data=json.dumps(data)
        # print(type(data))
        res = requests.post(url=url, data=data,headers=headers)
        print(res.text)

    def add_to_16(self,value):
        while len(value) % 16 != 0:
            value += '\0'
        # print(value.encode())
        return value.encode()  # 转成字节形式
    # 定义加密方法
    def encrypt_ecb(self,pt, key='KgRP3T9fezwGY769'):
        data = json.dumps(pt)
        # 1初始化加密器：128位key,ECB模式加密
        aes = AES.new(self.add_to_16(key), AES.MODE_ECB)
        # 2.处理数据块-128位,pkcs7模式
        block = pad(pt.encode('utf8'), 16)
        # 3.加密数据块
        tmp = aes.encrypt(block)
        # 4.base64编码数据 param=gHuFO4GClE5DbDXPQBw%2B7HTsv4RK2TAzMhOAfuy%2FDJk%3D
        ct = base64.encodebytes(tmp).decode()
        return ct
    #数据统计
    def Sjtj(self):
        EncryptKey = "KgRP3T9fezwGY769"
        AppKey = "2d2fb421-e2e0-47cd-b88c-573982f83abb"
        appId = 1000
        langCode = "en-US"
        # 获取时间戳
        t = int(time.time())
        # print(t)
        data_chong = {

        }
        # 加密参数
        data_chong = json.dumps(data_chong)
        print('param加密前为：' + data_chong)
        param = self.encrypt_ecb(data_chong)

        param = param.replace("\n", "")
        print('param加密后为：' + param)
        # param="/t+xYFvu21uTTTq9I5n2sFU3NiLzNf645H5su0yIkLo="
        # python使用MD5加密
        str_param = str(appId) + str(param) + str(t) + str(langCode) + str(AppKey)
        # str='this is a md5 test'
        m = hashlib.md5()
        b = str_param.encode(encoding='utf-8')
        m.update(b)
        str_md5 = m.hexdigest()
        print('MD5加密前为:' + str_param)
        print('MD5加密后为:' + str_md5)
        # 数据统计
        url = "http://mwsys-open-api.nn722.com/open_api/live/getCCUList"
        data = {
            "appId": 1000,
            "sign": str_md5,
            "param": param,
            "timestamp": t,
            "langCode": "en-US",
        }
        headers = {
            "Content-Type": "application/json"
        }
        data = json.dumps(data)
        # print(type(data))
        res = requests.post(url=url, data=data, headers=headers)
        print(res.text)
    #直播数据
    def zbsj(self):
        EncryptKey = "KgRP3T9fezwGY769"
        AppKey = "2d2fb421-e2e0-47cd-b88c-573982f83abb"
        appId = 1000
        langCode = "en-US"
        # 获取时间戳
        t = int(time.time())
        # print(t)
        data_chong = {

        }
        # 加密参数
        data_chong = json.dumps(data_chong)
        print('param加密前为：' + data_chong)
        param = self.encrypt_ecb(data_chong)

        param = param.replace("\n", "")
        print('param加密后为：' + param)
        # param="/t+xYFvu21uTTTq9I5n2sFU3NiLzNf645H5su0yIkLo="
        # python使用MD5加密
        str_param = str(appId) + str(param) + str(t) + str(langCode) + str(AppKey)
        # str='this is a md5 test'
        m = hashlib.md5()
        b = str_param.encode(encoding='utf-8')
        m.update(b)
        str_md5 = m.hexdigest()
        print('MD5加密前为:' + str_param)
        print('MD5加密后为:' + str_md5)
        # 数据统计
        url = "http://mwsys-open-api.nn722.com/open_api/live/getLiveList"
        data = {
            "appId": 1000,
            "sign": str_md5,
            "param": param,
            "timestamp": t,
            "langCode": "en-US",
        }
        headers = {
            "Content-Type": "application/json"
        }
        data = json.dumps(data)
        # print(type(data))
        res = requests.post(url=url, data=data, headers=headers)
        print(res.text)
    #打赏数据
    def dssj(self):
        EncryptKey = "KgRP3T9fezwGY769"
        AppKey = "2d2fb421-e2e0-47cd-b88c-573982f83abb"
        appId = 1000
        langCode = "en-US"
        # 获取时间戳
        t = int(time.time())
        # print(t)
        data_chong = {
        "liveId":34896
        }
        # 加密参数
        data_chong = json.dumps(data_chong)
        print('param加密前为：' + data_chong)
        param = self.encrypt_ecb(data_chong)

        param = param.replace("\n", "")
        print('param加密后为：' + param)
        # param="/t+xYFvu21uTTTq9I5n2sFU3NiLzNf645H5su0yIkLo="
        # python使用MD5加密
        str_param = str(appId) + str(param) + str(t) + str(langCode) + str(AppKey)
        # str='this is a md5 test'
        m = hashlib.md5()
        b = str_param.encode(encoding='utf-8')
        m.update(b)
        str_md5 = m.hexdigest()
        print('MD5加密前为:' + str_param)
        print('MD5加密后为:' + str_md5)
        # 数据统计
        url = "http://mwsys-open-api.nn722.com/open_api/live/getOrderList"
        data = {
            "appId": 1000,
            "sign": str_md5,
            "param": param,
            "timestamp": t,
            "langCode": "en-US",
        }
        headers = {
            "Content-Type": "application/json"
        }
        data = json.dumps(data)
        # print(type(data))
        res = requests.post(url=url, data=data, headers=headers)
        print(res.text)
    #转赠记录 /open_api/account/getTransferList
    def zzjl(self):
        EncryptKey = "KgRP3T9fezwGY769"
        AppKey = "2d2fb421-e2e0-47cd-b88c-573982f83abb"
        appId = 1000
        langCode = "en-US"
        # 获取时间戳
        t = int(time.time())
        # print(t)
        data_chong = {

        }
        # 加密参数
        data_chong = json.dumps(data_chong)
        print('param加密前为：' + data_chong)
        param = self.encrypt_ecb(data_chong)

        param = param.replace("\n", "")
        print('param加密后为：' + param)
        # param="/t+xYFvu21uTTTq9I5n2sFU3NiLzNf645H5su0yIkLo="
        # python使用MD5加密
        str_param = str(appId) + str(param) + str(t) + str(langCode) + str(AppKey)
        # str='this is a md5 test'
        m = hashlib.md5()
        b = str_param.encode(encoding='utf-8')
        m.update(b)
        str_md5 = m.hexdigest()
        print('MD5加密前为:' + str_param)
        print('MD5加密后为:' + str_md5)
        # 数据统计
        url = "http://mwsys-open-api.nn722.com/open_api/account/getTransferList"
        data = {
            "appId": 1000,
            "sign": str_md5,
            "param": param,
            "timestamp": t,
            "langCode": "en-US",
        }
        headers = {
            "Content-Type": "application/json"
        }
        data = json.dumps(data)
        # print(type(data))
        res = requests.post(url=url, data=data, headers=headers)
        print(res.text)
    #转赠金币/open_api/account/transfer
    def zzjb(self):
        EncryptKey = "KgRP3T9fezwGY769"
        AppKey = "2d2fb421-e2e0-47cd-b88c-573982f83abb"
        appId = 1000
        langCode = "en-US"
        # 获取时间戳
        t = int(time.time())
        # print(t)
        data_chong = {
            'fromUserId':'ml@8097937',
            'toUserId':'mw@10',
            'amount':1000,
            'orderId':'124545123'
        }
        # 加密参数
        data_chong = json.dumps(data_chong)
        print('param加密前为：' + data_chong)
        param = self.encrypt_ecb(data_chong)

        param = param.replace("\n", "")
        print('param加密后为：' + param)
        # param="/t+xYFvu21uTTTq9I5n2sFU3NiLzNf645H5su0yIkLo="
        # python使用MD5加密
        str_param = str(appId) + str(param) + str(t) + str(langCode) + str(AppKey)
        # str='this is a md5 test'
        m = hashlib.md5()
        b = str_param.encode(encoding='utf-8')
        m.update(b)
        str_md5 = m.hexdigest()
        print('MD5加密前为:' + str_param)
        print('MD5加密后为:' + str_md5)
        # 数据统计
        url = "http://mwsys-open-api.nn722.com/open_api/account/transfer"
        data = {
            "appId": 1000,
            "sign": str_md5,
            "param": param,
            "timestamp": t,
            "langCode": "en-US",
        }
        headers = {
            "Content-Type": "application/json"
        }
        data = json.dumps(data)
        # print(type(data))
        res = requests.post(url=url, data=data, headers=headers)
        print(res.text)
    #chongzhi /open_api/account/addmoney
    def chongzhi(self):
        EncryptKey = "KgRP3T9fezwGY769"
        AppKey = "2d2fb421-e2e0-47cd-b88c-573982f83abb"
        appId = 1000
        langCode = "en-US"
        # 获取时间戳
        t = int(time.time())
        # print(t)
        data_chong = {
            'type': 1,
            'userId	': 'mw@31',
            'amount': 1000,
            'orderNo': '124545123',
            'playAmount':10
        }
        # 加密参数
        data_chong = json.dumps(data_chong)
        print('param加密前为：' + data_chong)
        param = self.encrypt_ecb(data_chong)

        param = param.replace("\n", "")
        print('param加密后为：' + param)
        # param="/t+xYFvu21uTTTq9I5n2sFU3NiLzNf645H5su0yIkLo="
        # python使用MD5加密
        str_param = str(appId) + str(param) + str(t) + str(langCode) + str(AppKey)
        # str='this is a md5 test'
        m = hashlib.md5()
        b = str_param.encode(encoding='utf-8')
        m.update(b)
        str_md5 = m.hexdigest()
        print('MD5加密前为:' + str_param)
        print('MD5加密后为:' + str_md5)
        # 数据统计
        url = "http://mwsys-open-api.nn722.com/open_api/account/addmoney"
        data = {
            "appId": 1000,
            "sign": str_md5,
            "param": param,
            "timestamp": t,
            "langCode": "en-US",
        }
        headers = {
            "Content-Type": "application/json"
        }
        data = json.dumps(data)
        # print(type(data))
        res = requests.post(url=url, data=data, headers=headers)
        print(res.text)
if __name__ == '__main__':
    o=OpenTest()
    o.ChongZhi()
    o.Sjtj()
    o.zbsj()
    o.dssj()
    o.zzjl()
    o.zzjb()
    o.chongzhi()