import random

class Die ():
    """создание кубика"""
    def __init__(self):
        self.sides = 6

    def roll_die(self, y, z=6):
        """ 'y'= количество брасков, 'z'= количество чисел на кубике """
        for x in range(y):
            x = random.randint(1, z)
            self.sides = x
            print(self.sides)



cb = Die()
cb.roll_die(10, 10)



