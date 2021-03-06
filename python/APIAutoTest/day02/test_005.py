'''
fixtrue的作用域
1.默认是函数级别的
2.函数级别->模块级别->类级别->Session级别
'''

#模块级别

import pytest

#scope设置作用域，取值范围function、module、class、session
@pytest.fixture(scope='module')
def login():
    print("登录系统")#yeild之前是前置
    yield
    print("退出系统")#yeild之后是后置

@pytest.fixture(scope='module')
def db():
    print("连接数据库")
    yield
    print("断开数据库连接")

def test_query(db):
    print("执行查询功能，不需要登录")

def test_add(login):#第一次使用fixtrue的地方执行前置
    print("执行添加功能")

def test_delete():
    print("执行删除功能")

def test_modify():#模块执行结束执行后置
    print("执行修改功能")