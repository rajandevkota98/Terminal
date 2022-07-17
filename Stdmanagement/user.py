import  mysql.connector as sql
import sys
try:
    conn=sql.connect(host='localhost',user='root',passwd='password',database='blood')
    cur = conn.cursor()
    cur.execute('create table user_table(username varchar(25) primary key,passwrd varchar(25) not null )')
    break
except:
    print('Try another name:')