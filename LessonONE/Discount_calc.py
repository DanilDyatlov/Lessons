class ArithmeticException(Exception):
    pass

class Calculator:
    def calculate_discount(self, prise: float, discount: int):
            if discount < 0 or discount > 100 or prise < 0:
                raise ArithmeticException("недопустимые аргументы")
            discount_price = (prise * discount) / 100 
            return prise - discount_price

if __name__ == '__main__':
    calc = Calculator
    prise = 200
    discount = 10
    print(f"Цена без скидки: {prise}")
    print(f"Скидка состовляет: {discount} %")
    print(f"Цена с учетом скидки: {calc.calculate_discount(prise=100, discount=10)}")

