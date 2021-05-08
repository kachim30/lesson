

class Battery():
    """Запас тока в акумуляторе в % def upgrade_battery (x) значения  акумулятора """
    def __init__(self, x=0):
        self.battery_size = x

    def batter(self, z):
        """для изменения запаса заряда"""
        if z < 0:
            self.battery_size -= int(z)
        elif z >= 0:
            self.battery_size += int(z)

    def fers(self):
        print(self.battery_size)




