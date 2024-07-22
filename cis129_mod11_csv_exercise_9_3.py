# cis129_modd11_csv_exercise_9_3.py
"""
Module 11 exercise 9.3
Dylan McCallum
07/21/2024


Writing Student Records To a CSV File 

This program allows the instructor to enter student data into a CSV file
such as first and last name, and three exams that the student has completed

"""
# import required modules

import csv

# declare global classes and variables

class Student:
    def __init__(self, f_name=str, l_name=str,
                 exam1=int, exam2=int, exam3=int
                 ):

        self.f_name = f_name
        self.l_name = l_name
        self.exam1 = exam1
        self.exam2 = exam2
        self.exam3 = exam3

    # returns string representation of Student Object
    def __repr__(self):

        person_info = f'{self.f_name} {self.l_name}'
        exam_info = f' {self.exam1}, {self.exam2}, {self.exam3}'
        student = person_info + exam_info
        return student
    
# declare main function to hold all program operations

def main():

    # initialize variables for while loop and function operations

    stop_input = 'no'
    classroom = []
    count = 1
    border = "*"

    # while loop waits for sentinel value
    while stop_input == 'no':

        # while loop to append students to csv

        while count != 0:

            # while loop to verify correct value inputs
            try:

                # wrapping user inputs into variables

                fname = str(input("Enter the student's first name: ")).title()

                # validates that both name only contains letters
                
                if not fname.isalpha():
                    print("Invalid input, only letters")
                    continue

                lname = str(input("Enter the student's last name: ")).title()

                if not lname.isalpha():
                    print("Invalid input, only letters")
                    continue

                student_name = fname + ' ' + lname

                # validates grade input from the user

                first_exam = int(input(f"{student_name}'s 1st grade?: "))
                second_exam = int(input(f"{student_name}'s 2nd grade?: "))
                third_exam = int(input(f"{student_name}'s 3rd grade?: "))

                # checks the score of the input to ensure its within boundary

                if first_exam > 100 or first_exam < 0:
                    print("Invalid input, enter a number between 0 and 100")
                    continue
                elif second_exam > 100 or second_exam < 0:
                    print("Invalid input, enter a number between 0 and 100")
                    continue
                elif third_exam > 100 or third_exam < 0:
                    print("Invalid input, enter a number between 0 and 100")
                    continue



                # validates if the answer is yes or no
                user_input = str(input("Stop updating? yes or no: ")).lower()

                if user_input == 'no':
                    stop_input = user_input
                elif user_input == 'yes':
                    stop_input = user_input
                else:
                    print("Enter yes or no")
                    continue

                # adds student to the class list
                if stop_input == 'no':

                    student = Student(fname, lname, 
                                      first_exam, second_exam, 
                                      third_exam
                                      )

                    classroom.append(student)
                    count += 1
                else:

                    # will add the last student entered into the list
                    student = Student(fname, lname, 
                                      first_exam, second_exam, 
                                      third_exam
                                      )

                    classroom.append(student)
                    count = 0

            except ValueError:
                print("You must enter a number for a grade")    
            else:
                print(classroom)

                # outputs variables in formatted csv file

                with open('grades.csv', mode='w', newline='') as grades:

                    print(f'{"Students":<10}{"Grades":<10}', file = grades)
                    print(f'{border * 16}\n', file = grades)

                    writer = csv.writer(grades)
                    for obj in classroom:

                        # takes the object values and loops them into a list

                        writer.writerow([obj.f_name, obj.l_name, 
                                         obj.exam1, obj.exam2, 
                                         obj.exam3]
                                         )

# invokes main function

main()