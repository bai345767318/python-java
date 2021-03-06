'''
数据库的操作
'''
import pymysql


def connect(db):
    '''
    连接数据库
    :param db: 数据库相关的信息，字典格式的
    :return: 连接对象
    '''
    host = db['host']
    port = db['port']
    user = db['user']
    pwd = db['pwd']
    name = db['name']
    try:
       conn = pymysql.connect(host=host,port=port,user=user,
                              password=pwd,database=name,charset='utf8')
       print("连接数据库成功")
       return conn
    except Exception as e:
        print(f"连接数据库失败，异常信息为：{e}")

def disconnect(conn):
    '''
    断开数据库连接
    :param conn: connect方法返回的连接对象
    :return: 无
    '''
    try:
        conn.close()
        print("断开数据库连接成功")
    except Exception as e:
        print(f"断开数据库连接失败，异常信息为：{e}")

def execute(conn,sql):
    '''
    执行sql语句
    :param conn: connect返回的连接对象
    :param sql: 要执行的语句
    :return: 无
    '''
    try:
        c = conn.cursor()#获取游标
        c.execute(sql)#使用游标执行sql语句
        conn.commit()#提交
        c.close()#关闭游标
        print(f"执行sql语句成功，{sql}")
    except Exception as e:
        print(f"执行sql语句失败，异常信息为：{e}")

def execute_query(conn,sql):
    '''
    执行sql查询类语句
    :param conn: connect返回的连接对象
    :param sql: 要执行的语句
    :return: 查询返回结果
    '''
    try:
        c = conn.cursor()#获取游标-----------
        row_count = c.execute(sql)#使用游标执行sql语句
        conn.commit()#提交
        a = c.fetchall()#返回多条记录(元组)-----------
        c.close()#关闭游标
        print(f"执行sql语句成功：{sql}")
        return list(a)
    except Exception as e:
        print(f"执行sql语句失败，异常信息为：{e}")

#测试代码，用完删除
if __name__ == '__main__':
    # db = {"host":"192.168.150.54","port":3306,"name":"apple","user":"root","pwd":"123456"}
    db = {"host": "jy001", "port": 4406, "name": "future", "user": "root", "pwd": "123456"}
    conn = connect(db)
    mobile = "18122553366"
    sql = f"delete from member where mobilephone={mobile}"
    execute(conn,sql)

    sql = f"select * from member"
    execute(conn, sql)
    a = execute_query(conn, sql)
    print("a0",a[0])
    print(len(a))


