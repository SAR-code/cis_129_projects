# cis129_mod11_exercise_9_1.py
"""
Module 11 exercise 9.1
Dylan McCallum
07/21/2024

Writing Grades To A Plain Text File

This program calculates grades from the class and returns the class average
and then stores the grades in a text file.

"""
# declare global variables and objects

# declare class object to hold the student name and grade

class Student:
    def __init__(self, name=str, grade=int):
        self.name = name
        self.grade = grade
        
    def __repr__(self):
        return (f"Name: {self.name}\n",
                f"Grade: {self.grade}\n"
                )

# declare main function to hold program operations

def main():
    print("Hello")
    
    # initialize variables for while loop
    
    stop_grading = 'no'
    class_grades = []
    count = 1
    
    
    while stop_grading == 'no':
        
        while count != 0:
            
            # attemp to receive correct value inputs for grades
            try:
                student_name = input("Enter the student's name: ")
                grade = int(input(f"What is {student_name}'s grade?: "))
                stop_grading = input("Stop grading? (yes/no): ")
            
                if stop_grading == 'no':
                    student = Student(student_name, grade)
                    class_grades.append(student)
                    count += 1
                else:
                    count = 0
            
            
            
            except ValueError:
                print("You must enter a name for student or number for grade")
        
            else:
                for obj in class_grades:
                    print(obj.name, obj.grade, sep=' ')
    
      
    # create a grades.txt to write and store grades into
    
    # with open('grades.txt', mode='w') as grades:
    #     grades.write('100 Dylan 98\n')
    #     grades.write('200 Alex 79\n')
    #     grades.write('300 Dan 84\n')



# invokes main function

main()