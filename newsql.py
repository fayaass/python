import mysql.connector

con=mysql.connector.connect(user='fayas',host='localhost',password='fayas@7994',database='batch8')
con.autocommit=True
cur=con.cursor()
# cur.execute("create database batch8")

# cur.execute("create table std (roll int,name text,age int)")

try:
    cur.execute("create table std (roll int,name text,age int)")
except:
    pass

rollno=int(input('enter the roll no :'))
name=input('enter the name :')
age=int(input('enter the age :'))

cur.execute("insert into std (roll,name,age) values(%s,%s,%s)",(rollno,name,age))
con.commit()