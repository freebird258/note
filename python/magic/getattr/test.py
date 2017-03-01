# coding=utf-8
class Api1(object):
    def __init__(self,path=''):
        self._path=path
 
    def __getattr__(self,name):
        #print self._path,name
        return Api1("%s/%s"%(self._path,name))
 
    # 定义一个Post方法来发送请求
    def post(self):
        print self._path
 
#GET /users/articles/index 
#api1 = Api1()
#api1.user.articles.index.post()

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
    def post(self,aa):
        print aa
 
#/users/Charlie/index 
#api2=Api2()
#api2.post1("111")
class UrlGenerator(object):
	def __init__(self, root_url):
		self.url = root_url
 
	def __getattr__(self, item):
		if item == 'get' or item == 'post':
			print self.url
		return UrlGenerator('{}/{}'.format(self.url, item))
 
 
url_gen = UrlGenerator('http://xxxx')
url_gen.users.show.get
