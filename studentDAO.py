# DAO connects to the database to get data and return the data back to the server
# DAO takes the info from the database as a tuple
# Convert the tuple into JSON and send to server

import mysql.connector


class studentDAO:
    db = ""

    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="datarep"
        )
        print("Connection made")

    def create(self, student):
        cursor = self.db.cursor()
        sql = "insert into student_info (surname, first_name, registered_modules) values (%s,%s,%s)"
        values = [
            student['surname'],
            student['first_name'],
            # student['student_id'], student_id, ,%s
            student['registered_modules']
        ]
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from student_info'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        # print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findByID(self, student_id):
        cursor = self.db.cursor()
        sql = "select * from student_info where student_id = %s"
        values = (student_id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)

    def update(self, student):
        cursor = self.db.cursor()
        sql = "Update student_info SET surname = %s, first_name = %s, registered_modules = %s  Where student_id = %s"
        values = [
            student['surname'],
            student['first_name'],
            student['registered_modules'],
            student['student_id']
        ]
        print(values)
        cursor.execute(sql, values)
        self.db.commit()

    def check_student(self, student_id):
        cursor = self.db.cursor()
        sql = "Select EXISTS(select student_id from student_info where student_id = %s) as CheckExists"
        values = (student_id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return result

    def delete(self, student_id):
        cursor = self.db.cursor()
        sql = "delete from student_info where student_id = %s"
        values = (student_id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

    def convertToDict(self, result):
        colnames = ['surname', 'first_name', 'student_id', 'registered_modules']
        student = {}

        if result:
            for i, colname in enumerate(colnames):
                value = result[i]
                student[colname] = value
        return student

studentDAO = studentDAO()
