'''
Created on 2019年10月17日

@author: yxr
'''


import requests
from orca.debug import println

"""
  requests库的7个主要方法
  request（） 构造一个请求，支撑一下各方法的基础方法
  get() 获取HTML网页的主要方法，对应于HTTP的get方法
  head()获取HTML网页头信息，对应于HTTP的HEAD
  post() post请求
  put() put请求
  patch() 向HTML网页提交局部修改请求，对应于HTTP的patch请求
  delete() delete请求
  
  req.encoding 如果header中不存在charset,则认为编码为ISO-88591-1
  req.apparent_encoding  根据网页内容分析出的编码方式 
"""
def test_01():
    req = requests.get("http://www.baidu.com")
    code = req.status_code #响应码，200 SUCCESS,404 FILE
    print("响应码-->",code)
    print("当前编码："+req.encoding)
    req.encoding = "utf-8" #content encoding
    print("修改后编码："+req.encoding)
    respMsg = req.text #HTTP response message
    print("响应信息-->",respMsg)
    print("\n")
    print( req.content) #response binary message
    
    
"""
  理解requests 库的异常
  requests.ConnectionError  :网络链接错误异常，如DNS查询失败，拒绝连接等
  requests.HTTPError :HTTP错误
  requests.URLRuired : URL缺失异常
  requests.TooManyRedirects 超过最大重定向次数，产生从定向异常
  requests.ConnectTimeout :连接远程服务超时异常
  request.Timeout :请求URL超时，产生超时异常
  
  requests.raise_for_status()  如果不是200，产生异常requests.HTTPError
"""    
# 爬取网页的通用代码方法
def test_02(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status() #如果不是200，产生异常requests.HTTPError
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Exception"
    

#-----------------------------------------------------------------------------  

"""
  HHTP协议对资源的操作
  1）get  : 请求获取URL位置的资源
  2）head ：请求回去URL位置资源的响应消息报告，即获得该资源的头部信息
  3）post :请求向URL位置的资源后，附加新的数据
  4）put : 请求向URL位置存储一个资源，覆盖原URL位置的资源
  5）patch : 请求局部更新URL位置资源，即改变该处资源的部分内容
  6）delete : 请求删除URL位置存储的资源

"""
"""
 {
 'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 
 'Connection': 'keep-alive', 'Content-Encoding': 'gzip', 
 'Content-Type': 'text/html', 
 'Date': 'Sat, 19 Oct 2019 12:27:13 GMT', 
 'Last-Modified': 'Mon, 13 Jun 2016 02:50:26 GMT', 
 'Pragma': 'no-cache',
  'Server': 'bfe/1.0.8.18'}
"""
def test_head():
    r =requests.head("https://www.baidu.com/")
    heads = r.headers
    print(r.headers)
    text = r.text
    print(text) #空的
    
"""
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "age": "15", 
    "name": "xiaobai"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "19", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.22.0"
  }, 
  "json": null, 
  "origin": "117.25.166.131, 117.25.166.131", 
  "url": "https://httpbin.org/post"
}

"""    
def test_post():
    payload = {'name':'xiaobai','age':'15'}
    r = requests.post("http://httpbin.org/post", data = payload)
    print(r.text)    
"""
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "age": "15", 
    "name": "xiaobai"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "19", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.22.0"
  }, 
  "json": null, 
  "origin": "117.25.166.131, 117.25.166.131", 
  "url": "https://httpbin.org/put"
}
"""    
def test_put():
    payload = {'name':'xiaobai','age':'15'}
    r = requests.put("http://httpbin.org/put", data = payload)
    print(r.text) 
   
   

#-----------------------------------------------------------------------------
""" 
 requests.request(method,url,**kwarge)  
 method:请求方式，对应get/put/post/put/patch/delete/options等7种，
 url : 获取页面的url链接 
 **kwargs:控制访问的参数，共13个 
  
   1)params:字典或 字节序列，作为参数增加到url中
      kv =  {'name':'xiaobai','age':'15'}
      url = 'http://python123.io/ws'
      r = requests.request('GET',url,params = kv)
      print(r.url)
   
    2)data:字典，字节序列或文件对象，作为request的内容
       kv =  {'name':'xiaobai','age':'15'}
      url = 'http://python123.io/ws'
      r = requests.request('GET',url,data = kv)
      print(r.url)
   
    3)json:  json格式数据，做为request的内容
       kv =  {'name':'xiaobai','age':'15'}
      url = 'http://python123.io/ws'
      r = requests.request('GET',url,json = kv)
      print(r.url)
   
    4)headers:字典，http定制头
      hd = { "User-Agent": "Chrome/10"}
      url = 'http://python123.io/ws'
      r = requests.request('GET',url,headers = hd)
    
    5)cookies:字典或者CookieJar,requests中的cookies
    
    6)auth: 元组，支持http认证功能
    
    7）files:字典类型，传输文件
    fs = {'file':open('data.xls','rb')}
    url = 'http://python123.io/ws'
    r = request.request('post',url,files =fs)
      
    8)timeout：设置超时时间，秒为单位
     url = 'http://python123.io/ws'
     r = request.request('post',url,timeout = 10)
     
    9)proxies:字典类型，设定访问代理服务器，可以增加登入认证
    pxs = {
          'http':'http://user:pass@10.10.10.1:1234'
          'http':'https://10.10.10.1:4321'
          } 
    r = requests.request('GET','http://www.baidu.com',proxies = pxs) 
    
    10)allow_redirects:True/False ,默认为True,重定向开关
    
    11）stream : True/False,默认为True,获取内容立即下载开关
    
    12）verify: True/False,默认为True,认证SSL证书开关
    
    13）cert:本地SSL证书路径
    
    
    
""" 

def test_params():
    kv =  {'name':'xiaobai','age':'15'}
    url = 'http://python123.io/ws'
    r = requests.request('GET',url,params = kv)
    print(r.url)#https://python123.io/ws?name=xiaobai&age=15


#-----------------------------------------------------------------------------  
"""
网络爬虫的尺寸：
 1）爬取网页，玩转网页：小规模，数据量小，爬取速度不敏感，requests库
 2）爬取系列网站：中规模，数据规模较大，爬取速度敏感，scrapy库
 3）爬取全网：大规模，搜索引擎，爬取速度关键，需要定制开发
 
网络爬虫的限制：
 1）来源审查：判断User-Agent进行限制
    检查来访HTTP协议头的User-Agent域，只响应浏览器或友好的爬虫的访问
    
 2）发布公告：Robots协议
    告知所有爬虫网站的爬去策略，要求爬虫遵循 
    
    
 ROBOTS协议
  1）Robots Exclusion Standard :网络爬虫排除标准   
  2）作用：告知所有爬虫网站的爬去策略，要求爬虫遵循 
  3）方式：在网站根目录下的rebots.txt文件   
  
 robots使用：
   网络爬虫：自动或人工识别robots.txt，再进行内容爬取
   约束性：robots协议是建议但非约束性，网络爬虫可以不遵守，但存在法律风险 
   
"""  
  
   
if __name__ == "__main__" :
    
    
    
    
    test_params()
#     test_put()
#     test_post()
#       test_head()
#     test_01()   
#     url = "http://www.baidu.com"
#     print(test_02(url))
    

















