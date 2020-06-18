# import xlrd
# from openpyxl import Workbook
#
# #获取当前目录
#
# #打开excel文件
# data=xlrd.open_workbook(filename='./testData/KXliveApiCase.xlsx')
# print(data)
# #获取excel中一个工作表
# # table=data.sheets()[0]
# # print(table)
# # table=data.sheet_by_index(0)
# #获取login页的sheet对象数据
# table=data.sheet_by_name('login')
# #获取login第一行（下标为0）的所有数据
# colnames=table.row_values(0)
# print('colname:',colnames)
# #获取所有的有效行数
# nrows=table.nrows
# print(nrows)
# list=[]
# for rownum in range(1,nrows):
#     row=table.row_values(rownum)#获取每一行的数据值
#     dict={}
#     for i in range(len(colnames)):
#         dict[colnames[i]]=row[i]
#     list.append(dict)
# print(list)
#
# names=data.sheet_names() #返回book中所有工作表名字
# print(names)


import  unittest
from ddt import  ddt,data,unpack

# if dict1.get('no')!=None:
#     dict1['no']=22
#     print(dict1)
# else:
#     print(dict1)
# #print(dict2.get('no'))
# list='lskldssd'
# print(list.find('88'))
# for item in test_data:
#     #print(item.get('no'))
#     print(item.items())
#     print(item.keys())
#     print(item.values())
# print(test_data)
#dict.clear()
# dict2=dict1.copy()
# res=dict1.get('no0')
# print(dict1)
# print(dict2)
# print(res)
# for item in test_data:
#     pass
# test_data=[{'no':1,'name':'tom'},{'no':2,'name':'alicy'}]
# @ddt
# class TestMath(unittest.TestCase):
#     def setUp(self):
#         pass
#
#     @data(*test_data)   #脱外套只能一层
#     @unpack  #在“脱外套”之后，针对你拿到的每一条数据根据逗号进行拆分
#     def test_print_data(self,item):
#         if item.get('no')!='default':
#             print(item['no'])
#             print(item['name'])
#             print(type(item))
#         else:
#             pass
        # print(name)


# if __name__=="__main__":
#     unittest.main()

# list=[1,3]
# for i in list:
#     print(type(i))
#
#
# for j in range(2,4):
#     print(type(j))
# dict1={'no':1,'name':'tom'}
# dict2={'no':1,'name':'tom'}
# res=cmp(dict1, dict2)
# print(dict1.keys())

# count=0
# while count<5:
#     print(count,"比5小")
#     count=count+1
#
# else:
#     print(count,"大于等于5了")
#
# #flag = False
# name = 'python'
# if name == 'python1':  # 判断变量是否为 python
#     flag = True  # 条件成立时设置标志为真
#     print('welcome boss') # 并输出欢迎信息
#
# list=["sss"]
# if list:
#     print(list,type(list))
# else:
#     print("为空值")
# a=1
# b=2
# list=["1","a","888","b"]
# print(max(list))
#实例一
# count=0
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j and i!=k and k!=j:
#                 count=count+1
#                 print("符合要求的三位数：",i,j,k)
# print("符合要求的共有几个：",count)
#实例二
# input("请输入一个数字：")
# l=[]
# for i in range(0,3):
#     x=int(input("请输入一个数字：\n"))
#     #print(type(x))
#     print(l.append(x))
#
# l.sort()
# print(l)

# !/usr/bin/python
# -*- coding: UTF-8 -*-

# l = []
# for i in range(3):
#     x = int(input('integer:\n'))
#     l.append(x)
# l.sort()
# print(l)
# list1=[4,8,0,10]
# list2=['a','bda']
# for i in list2:
#     list1.append(i)
# # print(type(list1.append(list2)))
# print(list1)
# a=list1.count(4)
# print(a)
# # list1.clear()
# print(list1)
# list3=[]
# list3=list1.copy()
# print(list3)
# s = 'Hello\Charlie\Good\Morning'
# # print(s.upper())
# print(s.find('el',2,6))
# s.split('\\')
# print(s)
# str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
# print(str.split('a'))       # 以空格为分隔符，包含 \n
# print(str.split(' ', 2)) # 以空格为分隔符，分隔成两个
# tupe=(170538, 3802624, 0, 3, 2, 'mcmem/zb/19/10/14/1571020811575.jpg', None, 0, 1, 1571020862457, 1571020862457, 20, 0, 100001)
# id=tupe[0]
# member_id=tupe[1]
# preform=tupe[2]
# live_status=tupe[3]
# anchor_type=tupe[4]
# print("id=%s,member_id=%s,preform=%s,live_status=%s,anchor_type=%s"%(id,member_id,preform,live_status,anchor_type))
# l = [1, 2]
# i = ['a', 'b']
# dict([i,l])
# # print(type(dict[i]))
# # dict.values()
# dict1=dict([i,l])
# print(dict1.values())
# dict2=dict1.copy()
# print("dict2=%s"%dict2)
# es=dict1.items()
# print(s)
# str="llhpythopyll"
# if str.find("py")!=-1:
#     str.replace("py","lo",3)
#     print(str)
# dict = {'Name': 'Zara', 'Age': 7}
#
# print ("Value : %s" %  dict.values())

# import requests
# url='http://kxlive-node-api.nn722.com/user/register'
# header={"Content-Type":"application/json"}
# data={"phone": 18927500039,"password":"123456","platform":"kxlive",
#       "terminal":"pc","expire":10000,"ip":"183.63.114.61","userAgent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36","clientId":"abc","nickName":"${nickName}","smsCode":1234,"areaCode":86}
# res=requests.post(url,json=data,headers=header)
# print(res.json())
# import re
# p=re.compile('(a(b)c)d')
# print(p)
# m=p.match('abcd')
# print(m.group(0))
# for row in result:
#     id=row[0]
#     member_id=row[1]
#     preform_id=row[2]
#     live_status=row[3]
#     anchor_type=row[4]
#     print("id=%s,member_id=%s,preform=%s,live_status=%s,anchor_type=%s"%(id,member_id,preform_id,live_status,anchor_type))
# def func(a,b,c=1,*args, **kwargs):
#
#     for arg in args:
#         print(arg)
#
#     for kwg in kwargs:
#         print(kwg, kwargs[kwg])
#
#
# lis = [1, 2, 3]
# dic = {
#     'k1': 'v1',
#     'k2': 'v2'
# }
#
# func(2,3,*lis, **dic)
#
#
# def func(*args):
#     print(args)
#     for arg in args:
#         print(arg)
# func("haha",1,[],{})
# func(1,2,3,4)
import time
print(int(time.time()))
print(type(int(time.time())))
