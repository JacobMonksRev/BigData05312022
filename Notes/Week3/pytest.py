import unittest
from mytest import powers_of_2
import employee_example
import employee

# class MyTest(unittest.TestCase):
#     def testinsert(self):
#         m1 = employee.Manager("Bob",50000,"sales")
#         self.assertEqual(employee_example.insert_man(m1),"Manager Bob 50000 sales\n")

class MyTest2(unittest.TestCase):
    def testpowers(self):
        self.assertEqual(powers_of_2(4), 16)
    

if __name__ == '__main__':
    unittest.main()