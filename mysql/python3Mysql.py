#coding:utf-8
import mysql.connector
import sys, os

user = 'root'
pwd = 'micro1989'
host = 'localhost'
db = 'books'


data_file = 'mysql-test.dat'

create_table_sql = "CREATE TABLE IF NOT EXISTS mytable( \
                    id int(10) AUTO_INCREMENT PRIMARY KEY, \
                    name varchar(20), age int(4)) \
                    CHARACTER SET utf-8"

insert_sql = "INSERT INTO mytable(name, age) VALUES ('jay', 22 ), ('杰', 26)"
select_sql = "SELECT id, name, age FROM mytable"

cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
cursor = cnx.cursor()

try:
    cursor.execute(create_table_sql)
except mysql.connector.Error as err:
    print("create table 'mytable' failed")
    print("Error:{}".format(err.msg))
    sys.exit()
if os.path.exists(data_file)
    myfile = open(data_file)
    lines = myfile.readline()
    myfile.close()

    for line in lines:
        myset = line.split()
        sql = "INSERT INTO mytable (name, age) VALUES ('{}', '{}')".format(myset[0], myset[1])
        try:
            cursor.execute(sql)
        except mysql.connector.Error as err:
            print("insert table 'mytable' from file 'mysql-test.dat' --failed")
            print("Error:{}".format(err.msg))
            sys.exit()
try:
    cursor.execute(select_sql)
    for (id, name, age) in cursor:
        print("ID:{} Name:{} Age:{}".format(id, name,age))
except mysql.connector.Error as err:
    print("query table 'mytable' failed")
    print("Error:{}".format(err.msg))
    sys.exit()
cnx.commit()
cursor.close()
cnx.close()
