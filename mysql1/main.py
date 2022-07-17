import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost", user = "root", passwd= "password")
    cursor = mydb.cursor()
    cursor.execute("show databases")
    print(cursor.fetchall())
    s = "insert into new.nayatable values(101, 'Rajan','123')"
    # cursor.execute("create table new.nayatable(employe_id int(10), emp_name varchar(10), emp_mail_id varchar(20))")
    cursor.execute(s)
    mydb.commit()
    cursor.execute("select employe_id,emp_name from new.nayatable")
    print(cursor.fetchall())
except Exception as e:
    print(e)