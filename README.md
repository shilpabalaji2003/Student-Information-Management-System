# Student-Information-Management-System
This is a desktop application that stores and performs database operations on student records.
The entire project has been developed as a python package.
Concept used: Python-MySQL integration.
Python packages used: tkinter

# Database
The student databases have been created in the files project1.py and PROJECT2.py and have been stored in MySQL. Two types of student data are recorded: academic
data as well as personal data.
The academic data consists of the student's admission number, name, class, section and the marks obtained in 3 terms of the academic year.
The personal data consists of the student's admission number, name, class, section, father's name, mother's name, phone number and address.

# Main file
The main outline of the application (home page, login page and other structures) have been designed in the Project.py file.
All other modules of the project have been imported into this module.
Based on the type of user logged in (whether admin or student), the database can be accessed in 2 different ways:
- An admin can perform operations like displaying records, updating, searching or deleting records.
- A student can only view his/her academic or personal records.

# Academic records
This module extracts academic records from the student database where the admin can perform the said operations.

# Personal records
This module extracts personal records from the student database where the admin can perform the said operations.
