use datarep;

create table teacher_info(
    -> surname varchar(250),
    -> first_name varchar(250),
    -> teacher_id int AUTO_INCREMENT PRIMARY KEY,
    -> instructing_modules varchar(250)
    -> );
ALTER TABLE teacher_info AUTO_INCREMENT = 5550000;

create table student_info(
    -> surname varchar(250),
    -> first_name varchar(250),
    -> student_id int AUTO_INCREMENT PRIMARY KEY,
    -> registered_modules varchar(250)
    ->);
ALTER TABLE student_info AUTO_INCREMENT = 1110000;