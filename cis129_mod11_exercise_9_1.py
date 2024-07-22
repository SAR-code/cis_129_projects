# cis129_mod11_exercise_9_1.py
"""
Module 11 exercise 9.1, 9.2
Dylan McCallum
07/21/2024

Part 1
Writing Grades To A Plain Text File 

This program calculates grades from the class and returns the class average
and then stores the grades in a text file.

Part 2
Reading Grades From A Plain Text File

This program also reads grades from the class and returns the individual grade
and their total, count, and average

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

    # initialize variables for while loop and function operations

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

                student_name = str(input("Enter the student's name: ").title())

                # validates the name only contains letters
                if not student_name.isalpha():
                    print("Invalid input, only letters")
                    continue

                grade = int(input(f"What is {student_name}'s grade?: "))

                # validates grade input from the user
                if grade > 100 or grade < 0:
                   print("Invalid input, enter a number between 0 and 100")
                   continue

                user_input = str(input("Stop grading? Enter yes or no: ")).lower()

                # validates if the answer is a yes or no

                if user_input == 'no':
                    stop_grading = user_input
                elif user_input == 'yes':
                    stop_grading = user_input
                else:
                    print("Enter yes or no")
                    continue

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
                print("You must enter a number for grade")

            else:
                
                # stores the list of grades in a variable

                class_room_ave = get_class_total(grade_list)

                # outputs the variables into a formatted txt.file
                with open('grades.txt', mode='w') as grades:
                    print(f'{"Students":<10}{"Grades":<10}', file = grades)
                    print(f'{border * 16}\n', file = grades)

                    # gets the name and grade key value pairs from the obj
                    for obj in class_grades:
                        print(f'{obj.name:<10}{obj.grade:<10}',
                              file = grades
                              )

                    print(f"\nThe class average is {class_room_ave:.2f}",
                          file = grades
                          )

                print(f"{class_grades}\nclass average: {class_room_ave:.2f}")
    
    # this portion reads the file previously written
    
    with open('grades.txt', mode='r') as grades:
        print(f'\n{"Students":<10}{"Grades":<10}')
        print(f'{border * 16}\n')
        
        # gets the name and grade key value pairs from the obj
        for obj in class_grades:
            print(f'{obj.name:<10}{obj.grade:<10}')
        
        class_avg_r = get_class_total(grade_list)
        
        # outputs the individual grades, count, average, and total
        print(f"\nThe class average is: {class_avg_r:.2f}")
        print(f"The total class grade count is: {len(grade_list)}")
        print(f"The class grade total is: {sum(grade_list)}")


# function that calculates the class's grade average

def get_class_total(grades=list):

    # gets the sum of all grades
    class_sum = sum(grades)

    #gets the average of grades submitted
    class_avg = class_sum / len(grades)

    return class_avg

# invokes main function

main()