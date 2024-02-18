import sqlite3
import json
import xml.etree.ElementTree as ET


try:
    conn = sqlite3.connect("HyperionDev.db")
except sqlite3.Error:
    print("Please store your database as HyperionDev.db")
    quit()

contents = ""
f = open('HyperionDev.db', 'r+') # Open the file again!
for line in f:
    contents = contents + line
    print(contents)
    f.close()

cur = conn.cursor()

def usage_is_incorrect(input, num_args):
    if len(input) != num_args + 1:
        print(f"The {input[0]} command requires {num_args} arguments.")
        return True
    return False

def store_data_as_json(data, filename):
    pass

def store_data_as_xml(data, filename):
    pass

def offer_to_store(data):
    while True:
        print("Would you like to store this result?")
        choice = input("Y/[N]? : ").strip().lower()

        if choice == "y":
            filename = input("Specify filename. Must end in .xml or .json: ")
            ext = filename.split(".")[-1]
            if ext == 'xml':
                store_data_as_xml(data, filename)
            elif ext == 'json':
                store_data_as_json(data, filename)
            else:
                print("Invalid file extension. Please use .xml or .json")

        elif choice == 'n':
            break

        else:
            print("Invalid choice")

usage = '''
What would you like to do?

d - demo
vs <student_id>            - view subjects taken by a student
la <firstname> <surname>   - lookup address for a given firstname and surname
lr <student_id>            - list reviews for a given student_id
lc <teacher_id>            - list all courses taken by teacher_id
lnc                        - list all students who haven't completed their course
lf                         - list all students who have completed their course and achieved 30 or below
e                          - exit this program

Type your option here: '''

print("Welcome to the data querying app!")

while True:
    print()
    # Get input from user
    user_input = input(usage).split(" ")
    print()

    # Parse user input into command and args
    command = user_input[0]
    if len(user_input) > 1:
        args = user_input[1:]

    if command == 'd': # demo - a nice bit of code from me to you - this prints all student names and surnames :)
        data = cur.execute("SELECT * FROM Student")
        for _, first_name, last_name, _, _ in data:
            print(f"{first_name} {last_name}")
        
    elif command == 'vs': # view subjects by student_id
        if usage_is_incorrect(user_input, 1):
            continue
        student_id = args[0]
        data = None

        # Run SQL query and store in data
        query = "SELECT subject_name FROM Subjects WHERE student_id = ?"
        data = cur.execute(query, (student_id,)).fetchall()

        # Display the retrieved subjects
        for row in data:
            print(row[0])


        offer_to_store(data)
        pass

    elif command == 'la':# list address by name and surname
        if usage_is_incorrect(user_input, 2):
            continue
        firstname, surname = args[0], args[1]
        data = None

        # Run SQL query and store in data
        # Define SQL query to retrieve address for the given name and surname
        query = "SELECT address FROM Students WHERE firstname = ? AND surname = ?"
        data = cur.execute(query, (firstname, surname)).fetchall()

        # Display the retrieved address
        for row in data:
            print(row[0])

        offer_to_store(data)
        pass
    
    elif command == 'lr':# list reviews by student_id
        if usage_is_incorrect(user_input, 1):
            continue
        student_id = args[0]
        data = None

        # Run SQL query and store in data
        # Define SQL query to retrieve reviews for the student
        query = "SELECT review_text FROM Reviews WHERE student_id = ?"
        data = cur.execute(query, (student_id,)).fetchall()

        # Display the retrieved reviews
        for row in data:
            print(row[0])
        

        offer_to_store(data)
        pass
    
    elif command == 'lnc':# list all students who haven't completed their course
        data = None
        

        # Run SQL query and store in data
        query = "SELECT first_name, last_name FROM Student WHERE student_id = 0"
        data = cur.execute(query).fetchall()

        # Display the retrieved students
        for row in data:
            print(f"{row[0]} {row[1]}")

        offer_to_store(data)
        pass
    
    elif command == 'lf':# list all students who have completed their course and got a mark <= 30
        data = None

        # Run SQL query and store in data
        #  # Define SQL query to retrieve students who completed their course with mark <= 30
        query = "SELECT first_name, last_name FROM Student WHERE course = 1 AND mark <= 30"
        data = cur.execute(query).fetchall()

        # Display the retrieved students
        for row in data:
            print(f"{row[0]} {row[1]}")

        offer_to_store(data)
        pass
    
    elif command == 'e':# list address by name and surname
        print("Programme exited successfully!")
        break
    
    else:
        print(f"Incorrect command: '{command}'")
    

    
