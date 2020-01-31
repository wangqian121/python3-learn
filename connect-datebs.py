import pymysql
# 1.创建表
# #打开数据库连接，主机地址，端口号3306，用户名，密码，数据库名，字符集
# db=pymysql.Connect(host="localhost",port=3306,user="root",passwd="12345678",db="stu",charset="utf8")
# #创建一个游标对象，cursor
# cursor=db.cursor()
# sql="""create table student(
#     id int not null,
#     name varchar(20),
#     age int
# )"""
# cursor.execute(sql)#执行sql语句
# db.close()
# print(db)
# 2.表中增加数据
# db=pymysql.Connect(host="localhost",port=3306,user="root",passwd="12345678",db="stu",charset="utf8")
# cursor=db.cursor()
# sql='''insert into student(id,name,age) values (1,"zhangsan",12)
# '''
# cursor.execute(sql)
# db.commit()
# db.close()
# 3.查询数据
# db=pymysql.Connect(host="localhost",port=3306,user="root",passwd="12345678",db="stu",charset="utf8")
# cursor=db.cursor()
# sql='''select * from student where id=1
# '''
# cursor.execute(sql)
# #date1=cursor.fetchone()获取单个对象
# date=cursor.fetchall()#获取多个对象
# db.close()
# print(date)
#4.更新数据和删除数据
db=pymysql.Connect(host="localhost",port=3306,user="root",passwd="12345678",db="stu",charset="utf8")
cursor=db.cursor()
# sql='''update student set age=age+1
# '''
sql1='delete from student where id=1'
sql2='delete from student where idd=1'
try:
    cursor.execute(sql1)
    cursor.execute(sql2)
    db.commit()
except Exception as e:
    db.rollback()#回滚，事务，一个事务就是一个不可分割的整体，要不都执行，要不都不执行
    print("出现异常")
db.close()