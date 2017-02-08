# encoding: utf-8
#!/usr/bin/env python

####type 创建类
#way1
class Foo(object):
    foo = True
    def greet(self):
        print 'hello world'
        print self.foo
#way2
def greet(self):
    print 'hello world'
    print self.foo
Foo = type('Foo', (object, ), {'foo': True, 'greet': greet})

##作用：控制类的生成，比如django ORM等。
