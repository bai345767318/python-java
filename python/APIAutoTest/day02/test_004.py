'''
fixture：测试前置和后置，比较常用的方式
1.命名方式比较灵活，不限于setup、teardown等命名方式。
2.使用比较灵活。
3.不需要import即可实现共享。
'''

import pytest

#测试前置
@pytest.fixture()#默认是函数级别
def login():
    print("登录系统")#yeild之前是前置
    yield
    print("退出系统")#yeild之后是后置

#测试脚本
def test_query():
    print("查询功能，不需要登录")


#使用方式1：将fixture作为参数传到脚本中，比较常用。
def test_add(login):
    print("添加功能，需要登录")

#使用方式2：使用装饰器usefixtures
@pytest.mark.usefixtures("login")
def test_delete():
    print("删除功能，需要登录")

