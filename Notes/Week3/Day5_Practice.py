"""1. Write a Python function that creates a Counter given an inputed list.
      Print out the contents of the Counter in order from most instances to least.
"""
from collections import Counter

def MyCounter(lst):
    c1 = Counter(lst)
    common = c1.most_common(len(lst))

    for i in range(len(common)):
        print(common[i][0], ":", common[i][1])

MyList = ["Jacob", "Rose", "Ryan", "Precious", "Rian", "Rose", "Jacob", "Jacob", "Ryan"]
MyCounter(MyList)

"""
2. Write a Python function that returns a list of namedtuples given a list of tuples.
   Your namedtuples should also include an extra element at the end that incorporates a datetime object.
"""
from collections import namedtuple
import datetime

def TupleNames(lst):
    OurNames = namedtuple("Students", ["name", "age", "dob", "time"])
    newlst = []
    for i in lst:
        newlst.append(OurNames(i[0], i[1], i[2], datetime.datetime.now().strftime("%X")))
    
    return newlst

MyList2 = [('John', 21, 2000), ('Ted', 34, 1988), ('Sarah', 12, 2010)]
newlist = TupleNames(MyList2)
for i in newlist:
    print(i)

"""
3. Write a Python function that takes in a file and returns a list of emails
   that are found in that file. Be sure to use RegEx.
"""
import re      # RegEx - Regular Expressions
import os      # this is necessary to read and write to files.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def emails():
    content = open('emails.txt', 'r')
    finding = re.findall('\S+@\S+', content.read())
    print(finding)
    content.close()

emails()

# Testing for errors and raising exceptions

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

x = input("Enter name, age, and year of birth separated by commas: ")
count = 0
for i in x:
    if i == ',':
        count += 1
if count > 2:
    raise Exception('You cannot have extra commas!')
count = 0
myfile = open('csv_example.csv', 'a')
myfile.write("\n"+str(x))
myfile.close()

# try-except example

try:
    x = int(input("Please enter a number: "))
except ValueError:
    print(ValueError)
    print("X must be a number!")
    x = 0
else:
    print(x*1.5)
finally:
    print(x + 90)