import unittest
from calculator import Calculator,FactorialFunc

class CalcTest(unittest.TestCase):
    """
    Test the add function from the calc library
    """
    
    def testSqrt(self):
        Choice = 2 
        result = Calculator([4],Choice)
        self.assertEqual(result,2.0)
        self.assertNotEqual(Calculator([16],Choice),2.0,"Answer is 4.0")
        self.assertNotEqual(Calculator([100],Choice),9.0,"Answer is 10.0")
        self.assertEqual(Calculator([5],Choice),2.23606797749979,"Answer is 2.0")
    def testFactorial(self):
        Choice = 3 
        self.assertEqual(Calculator([1],Choice),1,"Answer is 1.0")
        self.assertEqual(Calculator([2],Choice),2,"Answer is 2.0")
        self.assertNotEqual(Calculator([4],Choice),22,"Answer is 24.0")
        self.assertEqual(Calculator([5],Choice),120,"Answer is 120.0")
    def testNatLog(self):
        Choice = 4
        self.assertNotEqual(Calculator([1],Choice),1,"Answer is 0")
        self.assertEqual(Calculator([2],Choice),0.6931471805599453,"Answer is 0.6931471805599453")
        self.assertEqual(Calculator([10],Choice),2.302585092994046,"Answer is 2.302585092994046")
    def testPow(self):
        Choice = 5      
        self.assertEqual(Calculator([100,0],Choice),1.0,"Answer is 1.0")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        self.assertNotEqual(Calculator([2,2],Choice),5.0,"Answer is 4.0")
        self.assertEqual(Calculator([10,3],Choice),1000.0,"Answer is 1000.0")
        self.assertEqual(Calculator([5,4],Choice),625,"Answer is 625.0")

if __name__ == '__main__':
    unittest.main()