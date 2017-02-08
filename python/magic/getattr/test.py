# coding=utf-8
class Api1(object):
    def __init__(self,path=''):
        self._path=path
 
    def __getattr__(self,name):
        print self._path,name
        return Api1("%s/%s"%(self._path,name))
 
    # 定义一个Post方法来发送请求
    def post(self):
        print self._path
 
#GET /users/articles/index 
api1 = Api1()
api1.user.articles.index.post()

class Api2(object):
    def __init__(self,path=''):
        self._path=path
 
    def __getattr__(self,name):
        print "__getattr__: ",self._path,name
        return Api2("%s/%s"%(self._path,name))
 
    def __call__(self,args):
        print "call: ",self._path,args
        self._path="%s/%s"%(self._path,args)
        return Api2(self._path)
 
    # 定义一个Post方法来发送请求
    def post(self):
        print self._path
 
#/users/Charlie/index 
api2=Api2()
api2.test.users("Charlie").index("index1").post()
