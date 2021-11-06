CREATE DATABASE universitydb;

CREATE TABLE `universitydb`.`users` (
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `role` int NOT NULL,  
  `userID` int NOT NULL AUTO_INCREMENT,
   KEY(userID)
   );

CREATE TABLE `universitydb`.`faculty` (
  `firstName` VARCHAR(45) NOT NULL,
  `lastName` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `JOB` VARCHAR(45) NOT NULL,
  `facultyID` int NOT NULL AUTO_INCREMENT,
   KEY(facultyID)
  );

CREATE TABLE `universitydb`.`courses` ( 
  `className` VARCHAR(45) NULL,
  `professorName` VARCHAR(45) NULL,
  `studentList` VARCHAR(450) NULL,
  `roomNumber` VARCHAR(45) NULL,
  `classID` int NOT NULL,
  `creditHours` VARCHAR(45) NULL,
  `roomCapacity` int,
  `numStudents` VARCHAR(45) NULL,
  `syllabus` VARCHAR(45) NULL,
  PRIMARY KEY(`classID`)
  );

CREATE TABLE `universitydb`.`students` (
  `firstName` VARCHAR(45) NULL,
  `lastName` VARCHAR(45) NOT NULL,
  `studentID` int NOT NULL,
  `creditHours` VARCHAR(45) NULL,
  `year` int NOT NULL,
  `age` int NOT NULL,
  `Advisor` VARCHAR(45) NULL,
  PRIMARY KEY (`studentID`)
  );

CREATE TABLE `universitydb`.`enrollments` (
  `Student` int NOT NULL,
  `Course` int NOT NULL,
  PRIMARY KEY (`Student`,`Course`),
  CONSTRAINT `constr_enrollment_student_fk`
    FOREIGN KEY `student_FK` (`Student`) REFERENCES `students`(`studentID`)
    ON DELETE CASCADE,
   CONSTRAINT `Constr_enrollment_course_fk`
        FOREIGN KEY `course_FK` (`Course`) REFERENCES `courses` (`classID`)
        ON DELETE CASCADE
  );