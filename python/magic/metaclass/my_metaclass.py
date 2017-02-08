# encoding: utf-8
#!/usr/bin/env python

class PrefixMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # 给所有属性和方法前面加上前缀 my_
        _attrs = (('my_' + name, value) for name, value in attrs.items())  
        
        _attrs = dict((name, value) for name, value in _attrs)  # 转化为字典
        _attrs['echo'] = lambda self, phrase: phrase  # 增加了一个 echo 方法
        
        return type.__new__(cls, name, bases, _attrs)
 
class Foo(object):
    __metaclass__ = PrefixMetaclass   # 注意跟 Python3 的写法有所区别
    name = 'foo'
    def bar(self):
        print 'bar'

#pyton 3
#class Foo(metaclass=PrefixMetaclass):
#    name = 'foo'
#    def bar(self):
#        print 'bar'

class Bar(Foo):
    prop = 'bar'

if __name__ == '__main__':
	b = Bar()
	print b.my_name,b.my_prop,b.echo('hello')
