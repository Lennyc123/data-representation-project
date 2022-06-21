# Server File
# Maps the http requests to individual functions
# return back responses 
# Map urls to functions - keep simple

from logging import debug
from flask import Flask, jsonify, request, abort, send_from_directory

from studentDAO import studentDAO
from teacherDAO import teacherDAO

app = Flask(__name__,
            static_url_path='',
            static_folder='staticpages')

@app.route("/")
def homepage():
    return send_from_directory('staticpages', 'index.html')
    #"<p>Sample text</p>"
    

# Get All
@app.route("/students")
def getAllStudents():
    return jsonify(studentDAO.getAll())

# Get All
@app.route("/teachers")
def getAllTeachers():
    return jsonify(teacherDAO.getAll())

# Find by ID
@app.route("/students/<int:student_id>")
def findByIdStudent(student_id):
    foundStudent = studentDAO.findByID(student_id)

    return jsonify(foundStudent)

# Find by ID
@app.route("/teachers/<int:teacher_id>")
def findByIdTeacher(teacher_id):
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
    # # Delete commands no check
    # studentDAO.delete(student_id)
    # return jsonify({"done": True})

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
    # # Delete commands no check
    # teacherDAO.delete(teacher_id)
    # return jsonify({"done": True})

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