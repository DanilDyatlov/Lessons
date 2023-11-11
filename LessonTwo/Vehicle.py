from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, company: str, model: str, year_release: int, num_wheels: int, speed: float):
        self.company = company
        self.model = model
        self.year_release = year_release
        self.num_wheels = num_wheels
        self.speed = speed
        
    @abstractmethod
    def test_drive(self):
        pass

    @abstractmethod
    def park(self):
        pass
