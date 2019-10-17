'''
Created on 2019年10月17日

@author: yxr
'''


import requests

"""
  requests库的7个主要方法
  request（） 构造一个请求，支撑一下各方法的基础方法
  get() 获取HTML网页的主要方法，对应于HTTP的get方法
  head()获取HTML网页头信息，对应于HTTP的HEAD
  post() post请求
  put() put请求
  patch() 向HTML网页提交局部修改请求，对应于HTTP的patch请求
  delete() delete请求
"""
def test_01():
    req = requests.get("http://www.baidu.com")
    code = req.status_code #响应码
    print("响应码-->",code)
    req.encoding = "utf-8"
    respMsg = req.text
    print("响应信息-->",respMsg)
    
test_01()   