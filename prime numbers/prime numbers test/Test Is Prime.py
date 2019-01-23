import unittest
import aval2

class TestPrimeNUmber (unittest.TestCase):

    def test_IsPrime (self):
        inputNumber = int(input("Please enter a number to see if it's prime or not: "))
        result = aval2.isPrime(inputNumber)
        self.assertEqual (result, aval2.isPrime(inputNumber))
        
if __name__ == '__main__':
    unittest.main()