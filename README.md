# Capstone-Project-I-Databases
# Compulsory Task
Run SQLite and use .read create_database.sql to create a database called
HyperionDev.db.
Follow these steps by using lookup.py as a template:
● Create a program that allows a user to easily be able to make certain queries
in the database. When printing, only certain fields should show on console.
● In addition, after each query, the user should be given the option to either
save the resulting query in XML or JSON form. The user should also be given
the option to choose their filename.
○ When saving to XML or JSON, all fields in the specified table should
be included in the file.
● The user should be able to
○ View all subjects being taken by a specified student (search by
student_id).
■ On console, the subject name should only be shown
○ Look up an address given a first name and a surname.
■ Only the street name and city should be shown on the console.
○ List all reviews given to a student (search by student_id).
■ The completeness, efficiency, style and documentation scores
should be displayed on console, along with the review text.
○ List all courses being given by a specific teacher (search by
teacher_id).
■ Just the course name should be displayed on the console.
○ List all students who haven’t completed their course.
■ The student number, first and last names, email addresses and
course names should be shown on the console.
○ List all students who have completed their course and achieved a
mark of 30 or below.
■ The student number, first and last names, email addresses and
course names should be shown on the console. Their marks
should also be displayed
