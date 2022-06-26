# Python script for creating the database tables
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="datarep"
)

cursor = db.cursor()
sql = "CREATE TABLE teacher_info (surname varchar(250), first_name varchar(250), teacher_id int AUTO_INCREMENT PRIMARY KEY, instructing_modules varchar(250));"

sql2 = "CREATE TABLE student_info (surname varchar(250), first_name varchar(250), student_id int AUTO_INCREMENT PRIMARY KEY, registered_modules varchar(250));"


cursor.execute(sql)
cursor.execute(sql2)
