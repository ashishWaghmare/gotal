import unittest
from code import *

class MyFirstTests(unittest.TestCase):
  
  def test_hello(self):
    self.assertEqual('Hello, World!', hello())


if __name__ == '__main__':
    unittest.main()
