class Airplane:
    def __init__(self):
        self.speed = 0
    def set_speed(self, speed):
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

class Flytest():
    biplane = Airplane()
    biplane.set_speed(212)
    print(biplane.get_speed())
    boeing = Jet()
    boeing.set_speed(422)
    print(boeing.get_speed())
    x=0
    while x<4:
        boeing.accelerate()
        print(boeing.get_speed())
        if boeing.get_speed() > 5000:
            biplane.set_speed(biplane.get_speed() * 2)
        else:
            boeing.accelerate()
        x += 1
    print(biplane.get_speed())

Flytest()