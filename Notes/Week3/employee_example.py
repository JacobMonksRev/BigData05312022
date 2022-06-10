from lib2to3.pytree import Base

from psutil import users
import employee                                    # must import the file that contains the classes
import os
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))

listEmp = []                                        # create empty lists to save our information
listMan = []
listTrain = []

def insert_emp():
    emp1 = employee.Employee                                # first indicate the file name, then the class name
    emp1.name = input("Enter the employee's first name: ")  # user input the information
    for i in emp1.name:                                     # checks each individual character in emp1.name
        if not (i.isalpha() or i in ("'","-",".")) and i != ' ': # checks if the character is valid
            raise Exception("Name contained an invalid character.") # raise exception if the character is not valid
    while True:                                                     # loops indefinitely until broken
        try:                                                        # try to execute this block of code
            emp1.salary = int(input("Enter the employee's salary: "))
        except ValueError:                                          # if the try-block found an exception, tell the user and try again
            print(ValueError)
            print("Salary was not valid")
        else:                                                       # if there was NO exception, break the loop.
            break
    emp1.dept = input("Enter the employee's dept: ")
    for i in emp1.dept:                                     # checks each individual character in emp1.dept
        if not i.isalpha():                                 # checks if the character is valid
            raise Exception("Dept contained an invalid character.") # raise exception if the character is not valid
    myFile = open('newFile.txt', 'a')                       # open our file to save the info
    myFile.write(str(emp1.type_employee) + ' ' + str(emp1.name) + ' ' + str(emp1.salary) + ' ' + str(emp1.dept) + '\n')
    myFile.close()

    # listEmp.append((emp1.name, emp1.salary, emp1.dept))     # appends the user input into the list as a tuple
    # print(listEmp)                                          # prints all contents of the list

def insert_man():
    man1 = employee.Manager
    man1.name = input("Enter the manager's first name: ")
    for i in man1.name:                                     # checks each individual character in emp1.name
        if not (i.isalpha() or i in ("'","-",".")) and i != ' ': # checks if the character is valid
            raise Exception("Name contained an invalid character.") # raise exception if the character is not valid
    while True:                                                     # loops indefinitely until broken
        try:                                                        # try to execute this block of code
            man1.salary = int(input("Enter the employee's salary: "))
        except ValueError:                                          # if the try-block found an exception, tell the user and try again
            print(ValueError)
            print("Salary was not valid")
        else:                                                       # if there was NO exception, break the loop.
            break
    man1.dept = input("Enter the manager's dept: ")
    for i in man1.dept:                                     # checks each individual character in emp1.dept
        if not i.isalpha():                                 # checks if the character is valid
            raise Exception("Dept contained an invalid character.") # raise exception if the character is not valid
    myFile = open('newFile.txt', 'a')
    myFile.write(str(man1.type_employee) + ' ' + str(man1.name) + ' ' + str(man1.salary) + ' ' + str(man1.dept) + '\n')
    myFile.close()

    # listMan.append((man1.name, man1.salary, man1.dept))
    # print(listMan)

def insert_trainee():
    train1 = employee.Trainee
    train1.name = input("Enter the trainee's first name: ")
    for i in train1.name:                                     # checks each individual character in emp1.name
        if not (i.isalpha() or i in ("'","-",".")) and i != ' ': # checks if the character is valid
            raise Exception("Name contained an invalid character.") # raise exception if the character is not valid
    while True:                                                     # loops indefinitely until broken
        try:                                                        # try to execute this block of code
            train1.salary = int(input("Enter the employee's salary: "))
        except ValueError:                                          # if the try-block found an exception, tell the user and try again
            print(ValueError)
            print("Salary was not valid")
        else:                                                       # if there was NO exception, break the loop.
            break
    train1.dept = input("Enter the trainee's dept: ")
    for i in train1.dept:                                     # checks each individual character in emp1.dept
        if not i.isalpha():                                 # checks if the character is valid
            raise Exception("Dept contained an invalid character.") # raise exception if the character is not valid
    myFile = open('newFile.txt', 'a')
    # Opens the file and then writes all the attibutes in the line below
    myFile.write(str(train1.type_employee) + ' ' + str(train1.name) + ' ' + str(train1.salary) + ' ' + str(train1.dept) + '\n')
    myFile.close()

    # listTrain.append((train1.name, train1.salary, train1.dept))
    # print(listTrain)

def startup():                                  # the startup function is called below so that it can run
    while True:                                 # this will loop infinitely because the condition is always True
        print("Welcome! What you like to do?")  # create a menu to give the user options
        print("\t1. Insert new employee.")
        print("\t2. Insert new manager.")
        print("\t3. Insert new trainee.")
        print("\t4. View all employees")
        print("\t5. Quit")
        # We want to check for an error if the user inputs a non-integer value
        while True:
            try:
                sel = int(input("\nSelection: "))       # take the user input for the selection
            except ValueError:
                print(ValueError)
                print("Please Enter an Integer 1-5!")
            else:
                break
        if sel == 1:                            # if-else statement checks for each possible selection
            insert_emp()                        # runs the insert_emp() function defined above
        elif sel == 2:
            insert_man()
        elif sel == 3:
            insert_trainee()
        elif sel == 4:
            myFile = open('newFile.txt', 'r')   #reads content of the file where our info was saved
            for line in myFile:
                print(line)
            myFile.close()
        elif sel == 5:
            myFile = open('newFile.txt', 'w')
            myFile.write('')
            myFile.close()
            print("Thank you! Have a good day!")
            break                               # immediately break the loop
        else:
            print("Please make a valid input.")

startup() # This will run when the program starts