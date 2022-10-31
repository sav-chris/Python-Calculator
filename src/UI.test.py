import UI
import unittest

class TestUICalculator(unittest.TestCase):

    def test_display_operation(self):
        calc = UI.CalculatorUI()
        calc.display_operations()
        


if __name__ == '__main__':
    unittest.main()        

