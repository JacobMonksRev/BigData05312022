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
        Inheritance - A child class will inherit the attributes and methods from a parent class.
        Polymorphism - a child class(es) and parent class can contain the same functions that do different things.
            Ex. Animal class with a 'move()' function
                Snake will slither
                Dog will run
                Pengiun will waddle
                Falcon will fly
        Abstraction - the specific functions or attributes of a class can be abstracted away (or obscured) from the user
            Ex. Everyone has and uses a coffee machine
                Not everyone knows what a coffee machine actually 'does' on the inside.
                You input the coffee beans and water
                The coffee machine gives you coffee
            When you call a class, the attributes and functions are not necessarily known to you
            but if you know how the class works, then you can still use it.

            Classes have different access modifiers:
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

        Encapsulation - idea that the methods and attributes for a class can only be accessed under certain restrictions
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

                    
"""