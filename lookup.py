import sqlite3
import json
import xml.etree.ElementTree as ET

# Connect to the SQLite database
conn = sqlite3.connect('HyperionDev.db')
cur = conn.cursor()

def save_as_json(filename, data):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def save_as_xml(filename, data):
    root = ET.Element("data")
    for item in data:
        record = ET.SubElement(root, "record")
        for key, value in item.items():
            field = ET.SubElement(record, key)
            field.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def view_subjects_by_student(student_id):
    query = f"""
    SELECT c.course_name
    FROM Student s
    LEFT JOIN StudentCourse sc ON s.student_id = sc.student_id
    LEFT JOIN Course c ON sc.course_code = c.course_code
    WHERE s.student_id = '{student_id}';
    """
    data = cur.execute(query).fetchall()
    subjects = [row[0] for row in data]
    print("Subjects taken by the student:")
    for subject in subjects:
        print(subject)

    save_option = input("Do you want to save this data as JSON or XML? (json/xml/none): ").lower()
    if save_option == 'json':
        filename = input("Enter the JSON filename to save: ")
        save_as_json(filename, subjects)
    elif save_option == 'xml':
        filename = input("Enter the XML filename to save: ")
        save_as_xml(filename, subjects)

def lookup_address(first_name, last_name):
    query = f"""
    SELECT a.street, a.city
    FROM Student s
    JOIN Address a ON s.address_id = a.address_id
    WHERE s.first_name = '{first_name}' AND s.last_name = '{last_name}';
    """
    data = cur.execute(query).fetchone()
    if data:
        street, city = data
        print(f"Street: {street}")
        print(f"City: {city}")

def list_reviews_by_student(student_id):
    query = f"""
    SELECT r.completeness, r.efficiency, r.style, r.documentation, r.review_text
    FROM Review r
    WHERE r.student_id = '{student_id}';
    """
    data = cur.execute(query).fetchall()
    print("Reviews for the student:")
    for row in data:
        completeness, efficiency, style, documentation, review_text = row
        print(f"Completeness: {completeness}, Efficiency: {efficiency}, Style: {style}, Documentation: {documentation}")
        print(f"Review Text: {review_text}")

    save_option = input("Do you want to save this data as JSON or XML? (json/xml/none): ").lower()
    if save_option == 'json':
        filename = input("Enter the JSON filename to save: ")
        reviews = [{"completeness": c, "efficiency": e, "style": s, "documentation": d, "review_text": rt} for c, e, s, d, rt in data]
        save_as_json(filename, reviews)
    elif save_option == 'xml':
        filename = input("Enter the XML filename to save: ")
        reviews = [{"completeness": c, "efficiency": e, "style": s, "documentation": d, "review_text": rt} for c, e, s, d, rt in data]
        save_as_xml(filename, reviews)

def list_courses_by_teacher(teacher_id):
    query = f"""
    SELECT c.course_name
    FROM Course c
    WHERE c.teacher_id = '{teacher_id}';
    """
    data = cur.execute(query).fetchall()
    courses = [row[0] for row in data]
    print("Courses taught by the teacher:")
    for course in courses:
        print(course)

def list_students_not_completed():
    query = """
    SELECT s.student_number, s.first_name, s.last_name, s.email, c.course_name
    FROM Student s
    LEFT JOIN StudentCourse sc ON s.student_id = sc.student_id
    LEFT JOIN Course c ON sc.course_code = c.course_code
    WHERE sc.is_complete IS NULL;
    """
    data = cur.execute(query).fetchall()
    print("Students who haven't completed their course:")
    for row in data:
        student_number, first_name, last_name, email, course_name = row
        print(f"Student Number: {student_number}")
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Email: {email}")
        print(f"Course Name: {course_name}")

    save_option = input("Do you want to save this data as JSON or XML? (json/xml/none): ").lower()
    if save_option == 'json':
        filename = input("Enter the JSON filename to save: ")
        students = [{"student_number": sn, "first_name": fn, "last_name": ln, "email": e, "course_name": cn} for sn, fn, ln, e, cn in data]
        save_as_json(filename, students)
    elif save_option == 'xml':
        filename = input("Enter the XML filename to save: ")
        students = [{"student_number": sn, "first_name": fn, "last_name": ln, "email": e, "course_name": cn} for sn, fn, ln, e, cn in data]
        save_as_xml(filename, students)

def list_students_completed_below_30():
    query = """
    SELECT s.student_number, s.first_name, s.last_name, s.email, c.course_name, sc.mark
    FROM Student s
    JOIN StudentCourse sc ON s.student_id = sc.student_id
    JOIN Course c ON sc.course_code = c.course_code
    WHERE sc.is_complete = 1 AND sc.mark <= 30;
    """
    data = cur.execute(query).fetchall()
    print("Students who have completed their course with a mark of 30 or below:")
    for row in data:
        student_number, first_name, last_name, email, course_name, mark = row
        print(f"Student Number: {student_number}")
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Email: {email}")
        print(f"Course Name: {course_name}")
        print(f"Mark: {mark}")

    save_option = input("Do you want to save this data as JSON or XML? (json/xml/none): ").lower()
    if save_option == 'json':
        filename = input("Enter the JSON filename to save: ")
        students = [{"student_number": sn, "first_name": fn, "last_name": ln, "email": e, "course_name": cn, "mark": m} for sn, fn, ln, e, cn, m in data]
        save_as_json(filename, students)
    elif save_option == 'xml':
        filename = input("Enter the XML filename to save: ")
        students = [{"student_number": sn, "first_name": fn, "last_name": ln, "email": e, "course_name": cn, "mark": m} for sn, fn, ln, e, cn, m in data]
        save_as_xml(filename, students)

# Main program loop
while True:
    print("\nSelect an option:")
    print("1. View all subjects by a specified student (search by student_id)")
    print("2. Look up an address given a first name and a surname")
    print("3. List all reviews given to a student (search by student_id)")
    print("4. List all courses being given by a specific teacher (search by teacher_id)")
    print("5. List all students who haven't completed their course")
    print("6. List all students who have completed their course and achieved a mark of 30 or below")
    print("7. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        student_id = input("Enter the student_id: ")
        view_subjects_by_student(student_id)
    elif choice == '2':
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        lookup_address(first_name, last_name)
    elif choice == '3':
        student_id = input("Enter the student_id: ")
        list_reviews_by_student(student_id)
    elif choice == '4':
        teacher_id = input("Enter the teacher_id: ")
        list_courses_by_teacher(teacher_id)
    elif choice == '5':
        list_students_not_completed()
    elif choice == '6':
        list_students_completed_below_30()
    elif choice == '7':
        break

# Close the database connection
conn.close()
