import unittest
from solutions import uniqueChars

class TestSolutions(unittest.TestCase):

  def testUniqueChars(self):
    self.assertEqual(uniqueChars('Hello World'), False)
    self.assertEqual(uniqueChars('abcdefghijklmnopqrstuvwxyz'), True)



if __name__ == '__main__':
    unittest.main()