#Brett Fuller
#12/08/2024
#CSD 325  – Assignment 8.2

import json

with open('/Users/bmfuller/Documents/vscode/csd/csd-325/module-8/students.json') as f:
    students = json.load(f)

#Function that displays a message about the information being printed and the student info.
def displayStudentList(students, message=''):
    print()
    if(message != ''):
        print(message)
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']}, Email = {student['Email']}")

#Call the display students function with a message for the original list
displayStudentList(students, "Printing original Student List:")

#my info saved as newStudent
newStudent ={
        "F_Name": "Brett",
        "L_Name": "Fuller",
        "Student_ID": 98765,
        "Email": "bfuller@gmail.com"
    }
#Add my info to the students list
students.append(newStudent)
    
#Call the display students function with a message for the updated list
displayStudentList(students, "Printing updated Student List:")

#open the json file with write permissions and Write over the existing json file with the updated student list
with open('/Users/bmfuller/Documents/vscode/csd/csd-325/module-8/students.json', 'w') as writable:
    json.dump(students, writable, indent=4)

#notify the user that the file has been updated
print()
print("JSON file was updated with the new student info.")