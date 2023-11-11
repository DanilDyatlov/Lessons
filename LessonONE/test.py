import unittest
from Discount_calc import Calculator, ArithmeticException

class CalculatorTest(unittest.TestCase):
   def setUp(self):
    #!!!!! Если просто взять без self в первом тесте calc подсвечивается 
        self.calc = Calculator()
   
   def test_one(self):
    # Сравнение двух значений
    # В методе нужно указывать self, чтобы не ловить ошибку с предоставление аргументов 
        self.assertEqual(self.calc.calculate_discount(100,10), 90, "Ошибка")

   def test_two(self):
    # Использование self.assertRaises является стандартным способом тестирования вызова исключений в Python. 
    # Этот метод принимает тип исключения и вызываемую функцию, и проверяет, что функция вызывает исключение указанного типа.
    # Выполнение теста успешное. 
        self.assertRaises(ArithmeticException, self.calc.calculate_discount, 100, -10)

if __name__ == '__main__':
    unittest.main()
