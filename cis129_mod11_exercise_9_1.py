# cis129_mod11_exercise_9_1.py
"""
Module 11 exercise 9.1
Dylan McCallum
07/21/2024

Writing Grades To A Plain Text File

This program calculates grades from the class and returns the class average
and then stores the grades in a text file.

"""

# declare global variables & class objects to hold the student name and grade

class Student:
    def __init__(self, name=str, grade=int):
        self.name = name
        self.grade = grade
    
    # returns string representation of the Student Object
    def __repr__(self):
        return f"{self.name}: {self.grade}"
                

# declare main function to hold program operations

def main():
    
    # initialize variables for while loop
    
    stop_grading = 'no'
    class_grades = []
    grade_list = []
    count = 1
    border = "*"
    
    
    while stop_grading == 'no':
        
        # while loop to append students and grades to a list
        
        while count != 0:
            
            # attempt to receive correct value inputs for grades
            try:
                student_name = input("Enter the student's name: ")
                grade = int(input(f"What is {student_name}'s grade?: "))
                stop_grading = input("Stop grading? ( yes/no ): ")
            
                # adds student to the class list
                if stop_grading == 'no':
                    student = Student(student_name, grade)
                    grade_list.append(grade)
                    class_grades.append(student)
                    count += 1
                else:
                    
                    # will add the last student entered into the list
                    student = Student(student_name, grade)
                    grade_list.append(grade)
                    class_grades.append(student)
                    count = 0
            
            # catches and raises incorrect input
            except ValueError:
                print("You must enter a name for student or number for grade")
        
            else:
                # stores the list of grades in a variable
                
                class_room_average = get_class_total(grade_list)
                
                # outputs the variables into a formatted txt.file
                with open('grades.txt', mode='w') as grades:
                    print(f'{"Students":<10}{"Grades":<10}', file = grades)
                    print(f'{border * 16}\n', file = grades)
                    
                    # gets the name and grade key value pairs from the obj
                    for obj in class_grades:
                        print(f'{obj.name:<10}{obj.grade:<10}',
                              file = grades
                              )
                        
                    #print(class_grades, file = grades)
                    print(f"\nThe class average is {class_room_average}",
                          file = grades
                          )

# function that calculates the class's grade average

def get_class_total(grades=list):
    class_sum = sum(grades)
    class_avg = class_sum / len(grades)
    print(f"The class average is {class_avg:.2f}")
    return class_avg

# invokes main function

main()