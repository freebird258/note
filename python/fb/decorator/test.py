#!/usr/bin/env python
#coding=utf8

###简单装饰器
def query_data(query):
 
    def wrapper():
        query()
    return wrapper
 
@query_data
def query_user():
    print 'query some user'
 
#query_user() ###=》query_data(query_user)()


##################被装饰函数参数
def query_data(query):
 
    def wrapper(count):
        query(count)
    return wrapper
 
#@query_data
def query_user(count):
    print 'query some user limit  {count}'.format(count=count)
 
#query_user(count=100) ##=》query_data(query_user)(count=100)

##装饰器参数
def router(url):
 
    print 'router invoke url', url
 
    def query_data(query):
 
        print 'query_data invoke url', url
 
        def wrapper(count):
            query(count)
        return wrapper
    return query_data
 
@router('/user')          # 首先调用了router函数， 输出 router invoke url /user， 进行@装饰，输出 'query_data invoke url', url
def query_user(count):
    print 'query some user limit  {count}'.format(count=count)

query_user(count=100) ##=》router('/user')(query_user)(count=100)
