

class Battery():
    """Запас тока в акумуляторе в % def upgrade_battery (x) значения  акумулятора """
    def __init__(self, x=0):
        self.battery_size = x

    def batter_2(self, z):
        """для изменения запаса заряда"""
        if z < -0:
            self.battery_size -= -z
        elif z >= 0:
            self.battery_size += z

    def print_bar(self):
        print(str(self.battery_size) + "%")






