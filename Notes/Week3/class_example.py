import employee                                     # must import the file that contains the classes

listEmp = []                                        # create empty lists to save our information
listMan = []
listTrain = []

def insert_emp():
    emp1 = employee.Employee                                # first indicate the file name, then the class name
    emp1.name = input("Enter the employee's first name: ")  # user input the information
    emp1.salary = input("Enter the employee's salary: ")   
    emp1.dept = input("Enter the employee's dept: ")
    listEmp.append((emp1.name, emp1.salary, emp1.dept))     # appends the user input into the list as a tuple
    print(listEmp)                                          # prints all contents of the list

def insert_man():
    man1 = employee.Manager
    man1.name = input("Enter the manager's first name: ")
    man1.salary = input("Enter the manager's salary: ")
    man1.dept = input("Enter the manager's dept: ")
    listMan.append((man1.name, man1.salary, man1.dept))
    print(listMan)

def insert_trainee():
    train1 = employee.Trainee
    train1.name = input("Enter the trainee's first name: ")
    train1.salary = input("Enter the trainee's salary: ")
    train1.dept = input("Enter the trainee's dept: ")
    listTrain.append((train1.name, train1.salary, train1.dept))
    print(listTrain)

def startup():                                  # the startup function is called below so that it can run
    while True:                                 # this will loop infinitely because the condition is always True
        print("Welcome! What you like to do?")  # create a menu to give the user options
        print("\t1. Insert new employee.")
        print("\t2. Insert new manager.")
        print("\t3. Insert new trainee.")
        print("\t4. Quit")
        sel = int(input("\nSelection: "))       # take the user input for the selection
        if sel == 1:                            # if-else statement checks for each possible selection
            insert_emp()                        # runs the insert_emp() function defined above
        elif sel == 2:
            insert_man()
        elif sel == 3:
            insert_trainee()
        elif sel == 4:
            print("Thank you! Have a good day!")
            break                               # immediately break the loop
        else:
            print("Please make a vlaid input.")

startup() # This will run when the program starts