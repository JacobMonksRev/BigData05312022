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
def x_value(x):
    if x < 5:
            print("X is less than 5")
    elif x < 10:
            print("X is less than 10, but greater than 5")
    else:
            print("X is greater than 10")

x_value(16)
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
        floor division // (grab only the whole number)
            Ex. 5 // 3 = 1
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
            >>> var = 8
            >>> var /= 4
            >>> prnt(var)
            2
        Exponent Equals **=
        modulo equals %=
    Comparison Operators:
        == Check if equal
        > greater than
        < less than
        != Check if not equal
        >= greater than or equal to
        <= less than or equal to
    Logical Operators:
        AND - return true if both statements are true
            Ex. if x > 5 AND x < 10:
                    print("x is between 5 and 10")
        OR - return true if either statement is true
            Ex. if right_eye == closed OR left_eye == closed
                    print("depth perception is lost")
        NOT - returns the opposite
            Ex. if NOT sleep_status
                    print("person is awake")
    Identity Operators:
        IS - return true if both variables are the same object and take the same space in memory
            Ex. a = [1, 2]
                b = [3, 4]
                c = a
                if c is a:
                    print("A and C are the same.")
        IS NOT
    Membership Operators:
        IN 
            listofAnimals = ['cat', 'dog', 'mouse', 'bird']
            var = 'cat'
            Ex. if var in listofAnimals:
                    print("Cat is in the animal lsit")
        NOT IN
    Bitwise Operators:
        10011101
        & - and
        | - or
        ^ - xor (exclusive or)
        >> - right shift 1101110
        << - left shift

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
    List - ordered set of values, mutable (changeable)
        Mutable means it can be changed
        They do not need to be the same datatype
        Allows duplicate values
        Ex. newList = [3, 4.5, "Jacob", "Monks", complex(5,5)]

        You can access individual values from a list using []
        newList[0] = 3
        newList[1] = 4.5
        newList[2] = "Jacob"
        You can use negatives to find values at a specified distance from the end
        newList[-1] = complex(5,5) = 5 + 5i

        You can add new items to a list using 'append'

        newList.append(5)

        You can also put the contents of one list into another list using 'extend'
        
        newList = [0, 1, 2, 3, 4]
        newList2 = [5, 6, 7, 8, 9]
        newList.extend(newList2)
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        len() - return the size of the list

        Create a list of other lists
            newList = [(1, 2, 3),(4, 5, 6),(7, 8, 9)]

        List slicing - when you grab the elements of a list after/before certain indexes

            newList[0:2] - grabs first two elements
                The second index is exclusive
            newList[::] - second colon denotes there is an increment
                newList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                newList[::2]
                (0, 2, 4, 6, 8)
    Dictionary
        List of elements that is mutable
        Not ordered (except in certain versions of python)
        A list of key - value pairs
            MyDictionary = {
                "brand" : "Ford",
                "model" : "Focus",
                "year" : 2017
            }
        Keys cannot repeat in the same dictionary
        If a key were to be written twice, the first one is overwritten.
    Tuple
        Sorting multiple items in a single entity
        declared using ()
        Tuples are ordered, but they are immutable (unchangeable)

        Ex. new_tuple = ('value1', 'value2', 'value3')
    
    Set
        A collection that is unordered, immutable
        A set cannot contain duplicates

        newSet = {'apple', 'cherry', 'banana', 'banana', 'melon'}
        Set Operations just like mySQL
        - union to join sets
        - intersection to get the similar items
        - difference to get the different items

Interpreter vs Compiler
    Interpreter convert code into something more comprehensible for the machine
    and execute code line by line.
    Compiler convert code into a file and parse the file for errors before
    converting it into machine code.
    Compiler is slower to execute and also takes up more memory, but it is more efficient.

    Python is considered an 'interpreted' language
        The compiler does relatively little work compared to the interpreter

        Compiler doesn't know the difference between keywords and given identifiers.
        Therefore, you cannot name an entity the same name as a keyword.


Functions
    A block of code that does a specific unit of work
    A function runs when it is called
    A function is useful if you have code that you would like to re-use

    x_value(10)
    x_value(1)
    x_value(16)
        """
def powers_of_2(e = 5):
    return 2 ** e

result = powers_of_2()

print("Result is", result)

def mult(x, y):
    return x * y

print(mult(4, 8))

def do_nothing():
    pass

# You can set default parameters by declaring the parameter equal to a value:
# Ex. def powers_of_2(e = 5):

"""
    Higher Order Functions
        A function is considered a higher order if it takes
        a function as an argument or returns a function for output.
"""

print("The result of this math is", mult(5, powers_of_2(7)))
print("The result of this math is " + str(mult(5, powers_of_2(7))))

# Given an employee's salary and pay period, find out how much they make per pay period

def num_periods(period):
    return 52 / period

def salary_per_period(salary, period):
    return salary / num_periods(period)

print("Paid", salary_per_period(50000, 2), "every pay period")

user_var1 = int(input("Enter salary: "))
user_var2 = int(input("Enter pay period in weeks: "))

print("Paid", salary_per_period(user_var1, user_var2), "every pay period")

"""
lambda:

    A small, anonymous function
    Take any number of arguments
    But can only have one expression
"""

cube = lambda n : n ** 3
def expo(y):
    return lambda n : n ** y

myNumber = expo(3)
print(myNumber(4))

"""
Namespace:

    A collection of all variables and functions that are currently defined in a block of code
    Contain info about the object names, parameters, etc.
    If the scope of an object ends, it means its namespace ends as well.
"""
# def myfunction2():
#     var3 = var + 5
#     for i in range(10):
#         vari = i + var2
# def myfunction():
#     global var
#     var = 5 + 7
#     var = var / 2
#     if var > 10:
#         var3 = var - 10
#     else:
#         pass
#     var2 = 5 + 4
#     var2 = var3 + var
#     return var2

# myNum = myfunction()
# myNum2 = myfunction2()

"""
    Python has some built-in namespaces, which you can see by calling
    dir(__builtins__)

Object-Oriented Programming:
    A programming paradigm that revolves around classes and objects
    Encompasses a certain structure of programming
    Python is considered to be an object-oriented language, but it can also perform functional.
    Therefore, Python is multi-paradigmed

    Classes: A structure of blueprint for creating new objects
    Objects: An instance of a class, it may contain variations or
             adaptations of the class it is created from
    Four pillars of OOP:
        1. Inheritance - A child class will inherit the attributes and methods from a parent class.
        
        2. Polymorphism - a child class(es) and parent class can contain the same methods that do different things.
            Ex. Animal class with a 'move()' function
                Snake will slither
                Dog will run
                Pengiun will waddle
                Falcon will fly

        3. Abstraction - the specific functions or attributes of a class can be abstracted away (or obscured) from the user
                    - handles complexity by hiding unnecessary details from the user
            Ex. Everyone has and uses a coffee machine
                Not everyone knows what a coffee machine actually 'does' on the inside.
                You input the coffee beans and water
                The coffee machine gives you coffee
            When you call a class, the attributes and functions are not necessarily known to you,
            but if you know how the class works, then you can still use it.

            Classes can have different access modifiers:
                1. Public, the default for a class
                2. Private, if a module instantiates a private class, that module cannot see the class's methods or variables
                3. Abstract, has defined methods (both abstract and non-abstract) but no implementation for those methods
                    Relies on the child classes to create implementations.
                    An abstract method is one that has defined parameters but no defined implementation
            Python does not do abstraction by default, you must import abstract base classes
                        import abc
                        from abc import ABC

            Abstract classes cannot be instantiated.

            Ex. class Shapes:
                    @abstractmethod
                    def number_sides(self)
                        pass

                class Octagon(Shapes):
                    def number_sides(self):
                        print("Number of sides is 8.")
                
                class Square(Shapes):
                    def number_sides(self):
                        print("Number of sides of 4.")

        4. Encapsulation - the idea that the methods and attributes for a class can only be accessed under certain restrictions
            Ex. People working in an office at a company.
                You work in marketing, and you need sales data for your work.
                Marketing team and sales team have their own responsibilities.
                Marketer cannot get the sales data unless they go directly through sales first.

            Protected members of a class:
                Methods or attributes are protected when they cannot be accessed outside of the class,
                but they can be accessed by child classes (use the underscore '_')

                Ex. class Workers:
                        def __init__(self):
                            # protected attribute
                            self._salesData = list[32.13, 65.89]
                        
                    class Marketer(Workers):
                        Workers.__init__(self)
                        print(self._salesData)

            Private members of a class:
                Methods or attributes that cannot be accessed anywhere
                except in the class they are a part of (use double underscore '__')
                Ex. class Workers:
                        def __init__(self):
                            # protected attribute
                            self.__salesData = list[32.13, 65.89]

            When to use encapsulation:
                You want certain values to remain unchanged or difficult to change accidentally.
                Adds a layer of security to all attributes and methods in your class.

Strings:
    A datatype that is a list of characters in quotes. 'My name is Jacob'
    Python is strongly typed
        It will not allow you to imply a change in datatype.
        Ex. 5 + '8' Will not execute
        You must indicate when you are changing datatypes of variables
    split() function splits apart a string based on a specific character, and can save each item in a list.
        str1 = 'cherry orange apple grape'
        listFruits = str.split()
        x = 5
        print('We have', x, 'fruit in our basket.')
        print('We have ' + str(x) + ' fruit in our basket.')
    strip() function removes whitespaces or newlines from the beginning and end of a string.
        str = '   Hello!     \n'
        print(str)
        print(str.strip())


Handling Files in Python:
    
    To open a file and refer to it later, you must save it in a variable:
    myFile = open('newFile.txt')
    
    To open a file to read it:
    myFile = open('newFile.txt', 'r')
    myFile.read()               - reads the whole file
    myFile.readline()           - reads starting from the pointer
    myFile.seek(0)              - reset the pointer to the beginning of the file
    myFile.seek(#)              - set the pointer at a specific line

    To open a file to write to it:
    myFile = open('newFile.txt', 'w')

    To open a file to append to the end of it:
    myFile = open('newFile.txt', 'a')

    When you are done with a file, be sure to close it:
    myFile.close()


Collection Modules:
    import collections

    These collections are not in the default namespace, but can be imported.

    Counter:
        from collections import Counter
        A subclass of dictionaries
        Keeps track of the number (count) of each value.

        list = ['apple','cherry','cherry','apple','orange','lemon']
        count_fruits = Counter(list)

    OrderedDict
        Another subclass of dictionary
        A dictionary that is ordered
        It remembers the order in which items are added to it
        Just like any other ordered collection, you can search them with indexes [#]

    DefaultDictionary
        Another subclass of dictionary
        Give a value to a key automatically if the key doesn't exist.

        d1 = defaultdict(int)

    ChainMap
        Encapsulates any number of different dictionaries and contains all of their keys and values
        Return a list of dictionaries
    
    Named Tuple
        Tuple with names given to the indexes.
        from collections import namedtuple

Datetime:
https://www.geeksforgeeks.org/python-strftime-function/
https://www.programiz.com/python-programming/datetime/strftime
    A datatype that contains the current time.
        Timestamp data.
    import datetime
    x = datetime.datetime.now()

Regular Expressions:
    Cheat Sheet
    https://www.geeksforgeeks.org/python-regex-cheat-sheet/
        Similar to LIKE keyword in MySQL
        Creates a pattern for matching its search

    import re
    x = 'Loraine sings in the rain in Spain'
    check_regex = re.findall('ain')

    Search for phone numbers:
        Phone numbers can be in different forms:
        1234568790
        123-456-8790
        (123) 456-7890

    Create a RegEx that can find each one in the following string.
        str = 'Johns phone number is 1234567890, but it used to be (532) 891-3123. Mary's is 432-435-5321'

Errors and Exceptions:
    An error is a problem in the code that the compiler / interpreter picks up
        Ex. x = int(input("Please enter a number: "))
        This will create a ValueError if the input is not information that can be converted into 'int'
        Errors normally occur:
            Syntax errors (incorrectly written code)
            Runtime errors (errors that occur when the proram tries to execute a command that cannot work)
        Exception is an error that occurs while the program is running.
            The terminal usually tells you the type of error tht occured

            ValueError
            FileNotFoundError
            TypeError
            DivideByZeroError

        You can create your own exceptions to occur when something happens that you do not want
        raise keyword
        

    Exception handling
        try-except block
        The code you think may create an exception goe in the try: block

        try:
            Code that could create an error
        except:
            Code that executes when an error is found
        else:
            Code that will execute if there are no errors
        finally:
            Code that will run regardless of errors or no errors.

MySQL Connector Python:
https://dev.mysql.com/downloads/connector/python/

Unit Testing:
- framework that is built off of Java JUnit
- testing each individual unit of a program.
    an individual function
    a class

- Validates each smallest portion of your program in order to ensure that they can all work as a whole.
- Python Unit Testing supports automation, set up and shutdown codes, and aggregation of test results.

import unittest

- Test Case:
    individual unit of testing
    setting a value for the test input and ensuring it gives the correct output
- Test Suite:
    multiple test cases done at once.
- Test Fixture:
    refers to any other resources needed for a test
        - extra servers for storage, a database connection, etc.
- Test Runner:
    Actual executor for the tests, provides the outcome to the user.

- A function can only be tested if it has a return value.

def printing(input):
    print(input)                # by itself, this cannot be tested.
    return str(input) + "newstring"   # adding this allows it to be tested

class MyTest(unittest.TestCase):
    def my_test(self):
        self.assertEqual()
        self.assertNotEqual()
        self.assertTrue()
        self.assertFalse()
        self.assertIs()
        self.assertIsNot()
        self.assertIsInstance()
        self.assertIsNotInstance()

Collection Comprehension:
- a short and concise way to create a new collection from one that already exists.
Ex. you want to take in a list of numbers, and create a list that has the even numbers among them.

- List Comprehension:
    list1 = [1,2,3,4,5,6,7,8,9]
    list2 = []
    list2 = [el for el in list1 if el % 2 == 0]

- Dictionary Comprehension
    dict2 = {key:value for (key,value) in dict2 if (key, value satisfies this)}
Ex. use a list of numbers to create a dictionary where keys and vlaues are the numbers followed bythe numbers squared.
    list1 = [1,2,3,4,5,6,7,8,9]
    dict1 = {}
    dict1 = {el:el**2 for el in list1}
    print(dict1)

- Set Comprehension
    Identical to lists except it can't have duplicates, and it uses {} instead of []
- Generator Comprehension
    This is also similar to lists, except it uses () instead of []
    Doesn't save the collection as a whole, instead it saves each individual value in memory.
    More memory efficient.

PyPI
- Python Package Index
- python's dedicated repository for importing modules and packages.
- Allows developers to create their own modules and then dliver them remotely so that other developers can easily access them.
- Developers can import the previously created libraries for their own purposes.
- Packages are just collecitons of modules.

pip
- Python package installer.
- can install packages from PyPI and elsewhere.
- pip commands
    pip search - searches for all PyPI packages
    pip install - install package
    pip uninstall - uninstall a previously installed package
    pip list - create a list of all currently installed packages
"""

