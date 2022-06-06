"""
PYTHON NOTES
What is Python?
Python is a general-purpose high-level programming language
    High-Level means human-readable
    Low level is machien-readable
Abstraction Levels:
    Machine Code - binary (1s and 0s)
    Assembly Code - invented in 1940s
                   - translate between high and low level code
    C Languages - higher level than Machien and Assembly
                 - contains limited keywords and is easy to learn
    Python - Very high-level
            - invented in 1991
            - Most popular programming language in the world
            - highly documented
    java - very high-level
          - invented in 1995
          - well documented
High level code is very easy to read, debug, and analyze

REPL - Read, Evaluate, Print, Loop
    It will run each line of code, print the result, and then loop to the next
    Any data created does not persist when you cloes the application
IDE - Integrated Development Environment
    VS Code
    IntelliJ

"""
x = 8
if x < 5:
        print("X is less than 5")
elif x < 10:
        print("X is less than 10, but greater than 5")
else:
        print("X is greater than 10")

"""
Python Statements:
    Simple Statement
    >>> x = 5
    Compound Statement
    >>> if x > 4:
            print("Hello")
    Loops:
    While Loop
    while(true):
        print("X is greatre than 5")
    For Loop
    for i in range(10):
        var = var + i

Python datatypes:
    int - integer
    string - characters
    float - decimals
    boolean - true/false
    complex - imaginary numbers

    To see the datatype of any entity, you can use: type()
    You can also change the type of data that something is:
        Use the datatype name a sa function
        Ex. 7 into a float =>
            var = 7
            var = float(var)

Python Operators:
    Math Operators
        Addition +
        subtraction -
        multiplication *
        division /
        modulo %
            Ex. 4 % 3 = 1
        exponent **
            Ex. 2 ** 3 = 8
    
    Assignment Operators:
        Equals =
        Plus Equals +=
            Ex. var += 5
        Minus Equals -=
        Multiply Equals *=
        Divide Equals /=
            var = 8
            var2 = var + 8
            var /= 4
        Exponent Equals **=
        modulo equals %=
    Comparison Operators:
    Logical Operators:
    Identity Operators:
    Membership Operators:
    Bitwise Operators:

If statement
    Will execute if a condition is true

    if var == 10:
        print(var)

You can expand an If statement by using elif (else-if)
Use to check for mlutiple conditions at a time

    if x < 5:
        print("X is less than 5")
    elif x < 10:
        print("X is less than 10, but greater than 5")
    else x > 10:
        print("X is greater than 10")

TO execute a .py file in terminal you run the command: py file_name.py

Collections:
    List - ordered set of values, mutable
        Mutable means it can be changed
        They do not need to be the same datatype
        Ex. newList = [3, 4.5, "Jacob", "Monks", complex(5,5)]

        You can access individual values from a list using []
        newList[0] = 3
        newList[1] = 4.5
        newList[2] = "Jacob"
        You can use negatives to find values at a specified distance from the end
        newList[-1] = complex(5,5) = 5 + 5i

        You can add new items to a list using 'append'

        newList.append(5)
        """