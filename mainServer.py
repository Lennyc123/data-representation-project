# Server File
# http requests are mapped to individual functions (python)
# Routing is established here i.e., urls


from logging import debug
from tkinter import EXCEPTION
from flask import Flask, session, redirect, url_for, render_template, escape, jsonify, request, abort, send_from_directory, g
from requests import Session

# Importing the data access objects for the tables within the database
from studentDAO import studentDAO
from teacherDAO import teacherDAO

# defining the parameters
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'


# Loging details are stored here
users = []
users.append(User(id=1, username='admin', password='admin'))


app = Flask(__name__)

# Flask secret key for sessions
app.secret_key = "admin[@2[,675;"

# Upon launching the server the user is directed to the login page
@app.route('/')
def begin():
    return redirect(url_for('login'))


@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

# Assess whether the user provided login information matches the stored login information
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        # If the username and password match the stored information continue to the profile page i.e., successfull authentication
        try:
            user = [x for x in users if x.username == username][0]
            if user and user.password == password:
                session['user_id'] = user.id
                return redirect(url_for('profile'))
        # If login attempt not successful return to the login screen
        except Exception:
            return redirect(url_for('login'))

    return render_template('login.html')

# Successful login screen
@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('profile.html')

# database selection screen, user can make crud commands to the database tables here
@app.route("/home")
def homepage():
    if not g.user:
        return redirect(url_for('login'))

    return send_from_directory('staticpages', 'index.html')


# Get All
@app.route("/students")
def getAllStudents():
    if not g.user:
        return redirect(url_for('login'))

    return jsonify(studentDAO.getAll())

# Get All
@app.route("/teachers")
def getAllTeachers():
    if not g.user:
        return redirect(url_for('login'))

    return jsonify(teacherDAO.getAll())

# Find by ID
@app.route("/students/<int:student_id>")
def findByIdStudent(student_id):
    if not g.user:
        return redirect(url_for('login'))

    foundStudent = studentDAO.findByID(student_id)

    return jsonify(foundStudent)

# Find by ID
@app.route("/teachers/<int:teacher_id>")
def findByIdTeacher(teacher_id):
    if not g.user:
        return redirect(url_for('login'))

    foundTeacher = teacherDAO.findByID(teacher_id)

    return jsonify(foundTeacher)

# Create
@app.route("/students", methods=['POST'])
def createStudent():
    if not request.json:
        abort(400)

    student = {
        "surname": request.json["surname"],
        "first_name": request.json["first_name"],
        # "student_id": request.json["student_id"],
        "registered_modules": request.json["registered_modules"]
    }
    return jsonify(studentDAO.create(student))

# Create
@app.route("/teachers", methods=['POST'])
def createTeacher():
    if not request.json:
        abort(400)

    teacher = {
        "surname": request.json["surname"],
        "first_name": request.json["first_name"],
        # "teacher_id": request.json["teacher_id"],
        "instructing_modules": request.json["instructing_modules"]
    }
    return jsonify(teacherDAO.create(teacher))

# Update
@app.route('/students/<int:student_id>', methods=['PUT'])
def updateStudent(student_id):
    found_Student = studentDAO.findByID(student_id)
    if found_Student == {}:
        return jsonify({}), 404
    currentStudent = found_Student
    if 'surname' in request.json:
        currentStudent['surname'] = request.json['surname']
    if 'first_name' in request.json:
        currentStudent['first_name'] = request.json['first_name']
    if 'registered_modules' in request.json:
        currentStudent['registered_modules'] = request.json['registered_modules']
    studentDAO.update(currentStudent)
    return jsonify(currentStudent)

# Update
@app.route('/teachers/<int:teacher_id>', methods=['PUT'])
def updateTeacher(teacher_id):
    found_Teacher = teacherDAO.findByID(teacher_id)
    if found_Teacher == {}:
        return jsonify({}), 404
    currentTeacher = found_Teacher
    if 'surname' in request.json:
        currentTeacher['surname'] = request.json['surname']
    if 'first_name' in request.json:
        currentTeacher['first_name'] = request.json['first_name']
    if 'instructing_modules' in request.json:
        currentTeacher['instructing_modules'] = request.json['instructing_modules']
    teacherDAO.update(currentTeacher)
    return jsonify(currentTeacher)

# Delete
@app.route('/students/<int:student_id>', methods=['DELETE'])
def deleteStudent(student_id):
    check_id = studentDAO.check_student(student_id)
    print(check_id)

    if check_id == (1,):
        studentDAO.delete(student_id)
        return jsonify({"Entry deleted": True})
    else:
        error_check = "Delete failed, as no entry with the provided ID found"
        return jsonify(error_check)

# Delete
@app.route('/teachers/<int:teacher_id>', methods=['DELETE'])
def deleteTeacher(teacher_id):
    check_id = teacherDAO.check_teacher(teacher_id)
    print(check_id)

    if check_id == (1,):
        teacherDAO.delete(teacher_id)
        return jsonify({"Entry deleted": True})
    else:
        error_check = "Delete failed, as no entry with the provided ID found"
        return jsonify(error_check)


if __name__ == "__main__":
    app.run(debug=True)