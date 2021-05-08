from lesson98 import Battery

class Car():
    """Простая модель автомобиля."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""
    def __init__(self, make, model, year):
       ### Инициализирует атрибуты класса-родителя.
        super().__init__(make, model, year)
        self.battery_1 = Battery.battery_size

    def print_batteri(self):
        print(self.battery_1 + '%')


my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.print_batteri()
my_tesla += Battery(100)
my_tesla.print_batteri()
