""""GLLAguilar
    DATALOG Prelims
    FEB. 26, 2020
    I have neither received nor provided any help
    on this Prelims, nor have I concealed
    any violation of the Honor Code.
"""


class Airplane:
    def __init__(self):
        self.speed = 0
    def set_speed(self,speed):
        self.speed = speed
    def get_speed(self):
        return self.speed

class Jet(Airplane):
    def __init__(self):
        self.MULTIPLIER = 2
    def set_speed(self,speed):
        super().set_speed(speed * self.MULTIPLIER)
    def accelerate(self):
        super().set_speed(self.get_speed() * 2)

class FlyTest():
    biplane = Airplane()
    biplane.set_speed(108)
    print(biplane.set_speed)
    boeing = Jet()
    boeing.set_speed(212)
    print(boeing.set_speed)
    x = 0
    while x >= 1:
        biplane.accelerate()
        print(biplane.set_speed)
        if biplane.accelerate > 5000:
            biplane.set_speed(biplane.get_speed() * 2)
        else:
            boeing.get_speed()
    print(biplane.get_speed)


FlyTest()