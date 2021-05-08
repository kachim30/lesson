from lesson98 import Battery
from lesson98Car import Car



class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""
    def __init__(self, make, model, year):
       ### Инициализирует атрибуты класса-родителя.
            super().__init__(make, model, year)
            self.battery_1 = Battery()

    def info_electricCar(self):
        print(self.get_descriptive_name() + "\n Зарядка:" + str(self.battery_1.battery_size) + '%')





my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.info_car()
my_tesla.battery_1.batter_2(30)
my_tesla.battery_1.print_bar()
my_tesla.battery_1.batter_2(40)
my_tesla.battery_1.print_bar()
my_tesla.battery_1.batter_2(-30)
my_tesla.battery_1.print_bar()

my_tesla.info_electricCar()

my_tesla.battery_1.batter_2(-30)

my_tesla.info_electricCar()
