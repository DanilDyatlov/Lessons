from Vehicle import Vehicle


class Car(Vehicle):
    def setUp(self):
        self.car = Car("BMW", "M5", 2020)
        
    def __init__(self, company, model, year_release):
        super().__init__(company, model, year_release, 4, 0)

    def test_drive(self):
        self.speed = 60

    def park(self):
        self.speed = 0

    def __repr__(self) -> str:
        return f"Car('{self.company}','{self.model}','{self.year_release}')"