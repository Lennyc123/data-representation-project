# Test file for assessing whether the data access object (python files) commands function as intended i.e., the crud commands
from studentDAO  import studentDAO

test1 = {
    'surname': 'O REILLY',
    'firstName': 'John',
    'registered_Modules': 'test',
    'student_ID': 21000 
}

test2 = {
    'surname': 'Madden',
    'firstName': 'Ellen',
    'registered_Modules': 'test' 
}


# returnvalue = studentDAO.create(test2)
# print(returnvalue)

# returnvalue = studentDAO.getAll()
# print(returnvalue)

# returnvalue = studentDAO.update(test1)
# print(returnvalue)

# returnvalue = studentDAO.delete(21001)
# print(returnvalue)

# returnvalue = studentDAO.delete(21014)
# print(returnvalue)

# returnvalue = studentDAO.findByID(21000)
# print(returnvalue)

# returnvalue = studentDAO.check_student(21006)
# print(returnvalue)