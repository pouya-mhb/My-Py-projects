import mymath
import unittest


class TestAdd(unittest.TestCase):

    def test_add_integers(self):

        result = mymath.add(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
  
        result = mymath.add(10.5, 2)
        self.assertEqual(result, 12.5)

    def test_add_strings(self):
     
        result = mymath.add('arash', 'rezaei')
        self.assertEqual(result, 'arashrezaei')


if __name__ == '__main__':
    unittest.main()
