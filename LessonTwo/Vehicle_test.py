import unittest
from Car import Car
from Motorcycle import Motorcycle


from Vehicle import *

class Vehicle_test(unittest.TestCase):

    def setUp(self) -> None:
        self.car = Car("BMW", "M5", 2020)
        self.moto = Motorcycle("Yamaha", "Yt", 2020)

    def instance_of(self):
        # Проверка на принадлежность
        # Функция isinstance() вернет True, если проверяемый объект object является экземпляром любого указанного в 
        # classinfo класса (классов) или его подкласса (прямого, косвенного или виртуального).
        # AssertIsInstance ( obj , cls , msg = None )
        
        # self.assertTrue(isinstance(self.car, Vehicle))
        self.assertIsInstance(self.car, Vehicle)

    def test_car_wheels(self):
        # Проверка на наличие 4 колес 
        self.assertEqual(self.car.num_wheels, 4, "Колеса") 
    
    def test_moto_wheels(self):
        # Проверка на наличие 2 колес
        self.assertEqual(self.moto.num_wheels, 2, "Колеса") 

    def test_car_speed(self):
        # Тестовое вождение 
        self.car.test_drive()
        self.assertEqual(self.car.speed, 60)

    def test_moto_speed(self):
        # Тестовое вождение 
        self.moto.test_drive()
        self.assertEqual(self.moto.speed, 75)

    def test_car_park_mode_after_test_drive(self):
        # Парковка 
        self.car.test_drive()
        self.car.park()
        self.assertEqual(self.car.speed, 0)

    def test_moto_park_mode_after_test_drive(self):
         # Парковка 
        self.moto.test_drive()
        self.moto.park()
        self.assertEqual(self.moto.speed, 0)

if __name__ == '__main__':
    unittest.main()