import requests
class BaseRequest():
    req=requests.Session()
    def get(self,url):
        resp=self.req.get(url)
        print('get')
        return resp
    def post(self,url):
        resp=self.req.post(url)
        print('post')
        return resp
    def put(self,url):
        resp=self.req.put(url)
        print('put')
        return resp
    #使用反射的方法
    def main_attr(self,method,url):
        if hasattr(self,method):
            print(method)
            func=getattr(self,method)
            print(func)
            func(url)
r=BaseRequest()
r.main_attr('get','http://www.baidu.com')
# r.main_attr('post','http://www.baidu.com')
# r.main_attr('put','http://www.baidu.com')




















