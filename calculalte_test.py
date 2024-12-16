import unittest
from calculator import calculator

class CalculatorTest(unittest.TestCase):
  def setUp(self):
    self.ergebnis1 = calculator(1,2,'+')
    self.ergebnis2 = calculator(1,2,'*')
    self.ergebnis3 = calculator(1,2,'/')
    self.ergebnis4 = calculator(1,2,'-')
    self.ergebnis5 = calculator(1,'+',3)
    self.ergebnis6 = calculator(1,2,'#')
    
  def test_calculate(self):
    self.assertTrue(self.ergebnis1 == 3)
    self.assertTrue(self.ergebnis2 == 2)
    self.assertTrue(self.ergebnis3 == 0.5)
    self.assertTrue(self.ergebnis4 == -1)
    self.assertTrue(self.ergebnis5 == 'Invalid Operator')
    self.assertTrue(self.ergebnis6 == 'Invalid Operator')
