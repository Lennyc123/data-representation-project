import mysql.connector


class teacherDAO:
    db = ""

    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="datarep"
        )
        print("Connection made")

    def create(self, teacher):
        cursor = self.db.cursor()
        sql = "insert into teacher_info (surname, first_name, instructing_modules) values (%s,%s,%s)"
        values = [
            teacher['surname'],
            teacher['first_name'],
            # teacher['teacher_id'], teacher_id, ,%s
            teacher['instructing_modules']
        ]
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from teacher_info'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        # print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findByID(self, teacher_id):
        cursor = self.db.cursor()
        sql = "select * from teacher_info where teacher_id = %s"
        values = (teacher_id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)

    def update(self, teacher):
        cursor = self.db.cursor()
        sql = "Update teacher_info SET surname = %s, first_name = %s, instructing_modules = %s  Where teacher_id = %s"
        values = [
            teacher['surname'],
            teacher['first_name'],
            teacher['instructing_modules'],
            teacher['teacher_id']
        ]
        print(values)
        cursor.execute(sql, values)
        self.db.commit()

    def check_teacher(self, teacher_id):
        cursor = self.db.cursor()
        sql = "Select EXISTS(select teacher_id from teacher_info where teacher_id = %s) as CheckExists"
        values = (teacher_id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return result

    def delete(self, teacher_id):
        cursor = self.db.cursor()
        sql = "delete from teacher_info where teacher_id = %s"
        values = (teacher_id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

    def convertToDict(self, result):
        colnames = ['surname', 'first_name', 'teacher_id', 'instructing_modules']
        teacher = {}

        if result:
            for i, colname in enumerate(colnames):
                value = result[i]
                teacher[colname] = value
        return teacher

teacherDAO = teacherDAO()


