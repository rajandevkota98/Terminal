import mysql.connector as connection
try:
    mydb = connection.connect(host= "localhost", password = "password",user = "root")

    cursor = mydb.cursor()
    # cursor.execute("create database suhanshu")
    # cursor.execute("show databases")
    # cursor.execute("create table suhanshu.ineuron(employee_id int)")
    cursor.execute("show databases")
    # cursor.execute("use suhanshu")
    # print(cursor.execute("selet * from suhanshu "))
    print(cursor.execute("select * from suhanshu.ineuron"))
    print(cursor.fetchall())

except Exception as e:
    print(e)



