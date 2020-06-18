import requests
import json
import requests

# s=requests.session() #创建一个会话
# req=s.get(url='')
#登录
#post=Http_reqest(post)
login_url='http://kxlive-node-api.nn722.com/user/login'
login_data={"phone": "18927509566",
            "password":"123456",
            "platform":"kxlive",
            "terminal":"pc",
            "expire":10000,
            "ip":"183.63.114.61",
            "userAgent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36",
            "clientId":"abc"}
login_head={"Content-Type":"application/json"}
login_res=requests.post(url=login_url,json=login_data,headers=login_head)
print(login_res.text)  #以str格式输出返回内容
print(login_res.json()) #以dict格式输出返回内容

#获取token值
token=login_res.json()['data']['token']
requests.get()

#抢红包
login_url='http://kxlive-node-api.nn722.com/user/login'
login_data={"phone": "18927509566",
            "password":"123456",
            "platform":"kxlive",
            "terminal":"pc",
            "expire":10000,
            "ip":"183.63.114.61",
            "userAgent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36",
            "clientId":"abc"}
login_head={"Content-Type":"application/json"}




#发评论
# reply_url='http://kxlive-node-api.nn722.com/community/reply'
# reply_data={"content": "接口发评论的内容",
#             "category":1,
#             "id":193}
# reply_head={"token":get_token(),
#             "Accept": "application/json",
#             "Content-Type":"application/json",
#             "userAgent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"}
# reply_res=requests.post(url=reply_url,json=reply_data,headers=reply_head)
# print(reply_res.json())










