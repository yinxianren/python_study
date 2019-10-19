'''
Created on 2019年10月19日

@author: yxr
'''
import requests


def test_jd():
    url = "https://item.jd.com/100006635632.html"
    try:
         r = requests.get(url)
         r.raise_for_status()
         r.encoding = r.apparent_encoding
         print(r.text)
    except:
       print("爬去失败")       
      
      
      
def  test_amazon():
    url = "https://www.amazon.cn/dp/B07Y9C684P"
    try:
        kv = {'user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}
        r = requests.get(url,headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
    except:
        print("fail")    
               
def test_baidu():
    kv = {'wd':'python'}
    try:
        r = requests.get("http://www.baidu.com/s",params= kv)
        print(r.request.url)
        r.raise_for_status()
        print(len(r.text))
    except:
        print("fail")                   
               
               
if __name__ == "__main__" :
    test_baidu()
               