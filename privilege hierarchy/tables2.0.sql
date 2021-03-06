CREATE DATABASE universitydb;

CREATE TABLE `universitydb`.`faculty` (
  `firstName` VARCHAR(45) NOT NULL,
  `lastName` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `JOB` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL);

CREATE TABLE `universitydb`.`courses` ( 
  `className` VARCHAR(45) NULL,
  `professorName` VARCHAR(45) NULL,
  `student list` VARCHAR(450) NULL,
  `roomNumber` VARCHAR(45) NULL,
  `classID` VARCHAR(45) NULL,
  `creditHours` VARCHAR(45) NULL,
  `roomCapacity` int,
  `registeredStudents` VARCHAR(45) NULL,
  `syllabus` VARCHAR(45) NULL
  );

CREATE TABLE `universitydb`.`students` (
  `firstName` VARCHAR(45) NULL,
  `lastName` VARCHAR(45) NOT NULL,
  `studentID` int NOT NULL,
  `creditHours` VARCHAR(45) NULL,
  `year` int NOT NULL,
  `age` int NOT NULL,
  `Advisor` VARCHAR(45) NULL,
  PRIMARY KEY (`eventID`));
