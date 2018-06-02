import unittest
from code import *

class MyFirstTests(unittest.TestCase):
  
  def test_hello(self):
    self.assertEqual('Hello, World!', hello())

  def test_bad_hello(self):
    self.assertEqual('Hello, World!', hello())

  def test_new_function(self):
    self.assertEqual(0, add())
  
  def test_five_return(self):
    self.assertEqual(5, add(2,3))


if __name__ == '__main__':
    import xmlrunner
    #unittest.main()
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))

