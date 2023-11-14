# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Celia Louie, 11/13/2023, Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
import json

MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a student for a course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
csv_data: str = ''
file = None
menu_choice: str
student_data: dict = {}
students: list = []


# When the program starts, read the file data
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
except FileNotFoundError as e:
    print("Text file must exist before running this script\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep="\n")
except Exception as e:
    print("There was a non-specific error\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep="\n")
finally:
    if not file.closed:
        file.close()


# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":
        try:
            # Check that first and last name input only contain letters
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should only contain letters")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should only contain letters")
        except Exception as e:
            print("There was a non-specific error\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep="\n")
        course_name = input("Enter the name of the course: ")
        student_data = {"student_first_name": student_first_name,
                        "student_last_name": student_last_name,
                        "course_name": course_name}
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f'Student {student["student_first_name"]} {student["student_last_name"]} is enrolled in {student["course_name"]}')
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            print("Registration has been saved")
        except FileNotFoundError as e:
            print("File must exist before running this script\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep="\n")
        except Exception as e:
            print("There was a non-specific error\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep="\n")
        finally:
            if not file.closed:
                file.close()
                continue

    # Stop the loop
    elif menu_choice == "4":
        break

    else:
        print("Please only choose option 1, 2, or 3")

print("Program ended")