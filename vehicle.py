class Vehicle(object):
    def __init__(self, name):
        self.speed = 0
        self.direction = 0
        self.color = "black"
        self.name = name

    def __repr__(self):
        return self.name

    def accelerate(self, x):
        print "from", self.speed,
        self.speed += max(0, x)
        print "to", self.speed

    def brake(self, x):
        print "from", self.speed,
        self.speed -= max(0, x)
        print "to", self.speed

    def turn_left(self):
        print "from", self.direction,
        self.direction -= 90
        print "to", self.direction

    def turn_right(self):
        print "from", self.direction,
        self.direction += 90
        print "to", self.direction


class ManualTrans(Vehicle):
    def __init__(self, name):
        super(ManualTrans, self).__init__(name = name)
        self.clutch_in = False

    def engage_clutch(self):
        self.clutch_in = True

    def disengage_clutch(self):
        self.clutch_in = False

    def brake(self, x):
        self.engage_clutch()
        super(ManualTrans, self).brake(x)

class ManualCar(ManualTrans):
    def __init__(self, name, color):
        super(ManualCar, self).__init__(name=name)
        self.color = color
        self.speed = 10

    def accelerate(self, x):
         super(ManualCar, self).accelerate(x)

    def engage_clutch(self):
        super(ManualCar, self).engage_clutch()


class RaceCar(ManualCar):
    def __init__(self, name, color):
        super(RaceCar, self).__init__(name=name, color=color)
        self.speed = 0

    def accelerate(self, x):
        super(RaceCar, self).accelerate(x)

class StreetCar(ManualCar):
    def __init__(self, name, color):
        super(StreetCar, self).__init__(name=name, color=color)

class MotorBike(ManualTrans):
    def __init__(self, name, color):
        super(MotorBike, self).__init__(name=name)
        self.wheels = 2

class AutoTrans(Vehicle):
    def __init__(self, name,color):
        super(AutoTrans, self).__init__(name=name)
        self.color = color
class AutoCar(AutoTrans):
    def __init__(self, name, color):
        super(AutoCar, self).__init__(name=name, color=color)

class Boat(AutoTrans):
    def __init__(self, name, color):
        super(Boat, self).__init__(name=name, color=color)
        self.floats = "your boat"
        #self.float_well = True
