# Data Representation Project
The files contained within this repository are related to a web application project.

--- 

## This project contains the following elements:

### A Flask server (*see mainServer.py*)
Within this python file the routing for the webpages was established [1]. A series of functions were created in order to perform **CRUD** operations and communicate with the Data Access Objects i.e., see studentDAO.py & teacherDAO.py

### A Database with two accompanying tables
A database (DB) was created using MySQL [2]. The DB is titled datarep, and the two tables are student_info & teacher_info.

### Web Interface
A user interface was established using HTML and AJAX calls to perform CRUD operations on the database tables (*See index.html, within the staticpages folder*) [3]. The user interface was styled using Bulma [4]. Bulma was imported using a CDN (Content Delivery Network).

`<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">`

### Authorization (logging in)
A login screen was established using Flask sessions(*see login.html & profile.html, within the template folder*) [5]

### Online Hosting
The contents of this web application project were hosted online using pythonanywhere [6]. http://lennyc123.pythonanywhere.com/login



# References
[1] Flask Documentation: https://flask.palletsprojects.com/en/2.1.x/

[2] Why MySQL: https://www.mysql.com/why-mysql/

[3] W3schools Ajax Introduction: https://www.w3schools.com/xml/ajax_intro.asp

[4] Bulma CSS Framework: https://bulma.io/

[5] Flask Sessions: https://www.tutorialspoint.com/flask/flask_sessions.htm

[6] Pythonanywhere: https://www.pythonanywhere.com/



