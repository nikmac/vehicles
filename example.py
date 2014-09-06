__author__ = 'GoldenGate'

class Vehicle(object):
    def __init__(self, color, name):
        self.speed = 0
        self.direction = 0
        self.color = color
        self.name = name
        self.turbo = False

    def __repr__(self):
        return self.name

    def accelerate(self):
        self.speed += max(0,1)

    def brake(self):
        self.speed -= max(0,1)

    def turn_left(self):
        self.direction -= 90

    def status(self):
        print "name: " + self.name
        print "speed: " + str(self.speed)
        print "turbo: " + str(self.turbo)

class ManualTrans(Vehicle):
    def __init__(self, color, name):
#super will inherit even the speed and direction of the parent class
        super(ManualTrans, self).__init__(color, name)
        self.clutch_in = False

    def engage_clutch(self):
        self.clutch_in = True

    def disengage_clutch(self):
        self.clutch_in = False

    def brake(self):
        self.engage_clutch()
        super(ManualTrans, self).brake()
        self.disengage_clutch()

class ManualCar(ManualTrans):
    def __init__(self, color, name, seats):
        super(ManualCar, self).__init__(color, name)
        self.seats= seats
        self.shift_type = "manual"


class CarMixin(object):
    def turbo_switch(self):
        if self.turbo == False:
            self.turbo = True
            self.speed += 10
        else:
            self.turbo = False
            self.speed -= 10

class Motorbike(ManualTrans, CarMixin):
    def __init__(self, color, name, seats = 2):
        super(Motorbike, self).__init__(color, name)
        self.seats = seats

    def add_third_wheel(self):
        self.seats += 1

def make_Motorbike():
    name = raw_input("what will be the name of this bike? ")
    color = raw_input("what color? ")
    bike = Motorbike(color = color, name= name)
    garage[name] = bike

class RaceCar(ManualCar, CarMixin):
    def __init__(self, color, name, seats):
        super(RaceCar, self).__init__(color,seats, name)
        self.turbo = False
        self.shift_type="manual"
        self.radio = False

    def push_turbo(self):
        if self.turbo == True:
            self.turbo = False
            self.speed -= 20
            print self.speed
        else:
            self.turbo = True
            self.speed += 20
            print self.speed

    def status(self):
        print "color: " + self.color
        print "seats: " + str(self.seats)
        print "turbo: " + str(self.turbo)
        print "speed: " + str(self.speed)
        print "radio: " + str(self.radio)
        print "shift type: " + self.shift_type

def make_RaceCar():
    name = raw_input("what will be the name of this racecar? ")
    color = raw_input("what color? ")
    seats = raw_input("how many seats will it have? ")
    race_car = RaceCar(color = color, name= name, seats = seats)
    garage[name] = race_car

class StreetCar(ManualCar, CarMixin):
    def __init__(self, color, name, seats):
        super(StreetCar, self).__init__(color, name, seats)
        self.shift_type="manual"

def make_StreetCar():
    name = raw_input("what will be the name of this streetcar? ")
    color = raw_input("what color? ")
    seats = raw_input("how many seats will it have? ")
    street_car = StreetCar(color = color, name= name, seats = seats)
    garage[name] = street_car

class AutoTrans(Vehicle):
    def __init__(self, color, name, turbo):
        super(AutoTrans, self).__init__(color, name, turbo)

class AutoCar(AutoTrans, CarMixin):
    def __init__(self, color, name, turbo, seats):
        super(AutoCar, self).__init__(color, name, turbo)
        self.seats = seats

def make_AutoCar():
    name = raw_input("what will be the name of this autocar? ")
    color = raw_input("what color? ")
    seats = raw_input("how many seats will it have? ")
    auto_car = AutoCar(color = color, name= name, seats = seats)
    garage[name] = auto_car

class Boat(AutoTrans):
    def __init__(self, color, name, turbo, seats):
        super(Boat, self).__init__(color, name, turbo)
        self.seats = seats

def make_Boat():
    name = raw_input("what will be the name of this boat? ")
    color = raw_input("what color? ")
    seats = raw_input("how many seats will it have? ")
    boat = Boat(color = color, name= name, seats = seats)
    garage[name] = boat


garage = {}
def make_car():
    response = raw_input("do you want to make a (v)ehicle? or (d)rive? ")
    if response == "v":
        response = raw_input("what do you want to make? \n" \
                   "(r)acecar?\n" \
                   "(s)treetcar\n" \
                   "(m)otorbike \n" \
                   "(a)utocar \n" \
                   "(b)oat   ")
        if response == "r":
            make_RaceCar()
            make_car()
        elif response == "s":
            make_StreetCar()
            make_car()
        elif response == "m":
            make_Motorbike()
            make_car()
        elif response == "a":
            make_AutoCar()
            make_car()
        elif response == "b":
            make_Boat()
            make_car()
    elif response == "d":
        drive()
def drive():
    if len(garage) > 0:
        for car in garage:
            print car
        chosen_car = raw_input("which car do you want to drive? ")
        if chosen_car in garage:
            print "let's drive " + chosen_car

            driving = True
            while driving == True:
                response = raw_input("what do you want to do? \n" \
                    "(a)ccelerate \n" \
                    "(b)rake \n" \
                    "(t)urbo switch \n"
                    "(r)eturn to garage \n"
                    "(s)tatus")
                if response == "a":
                    garage[chosen_car].accelerate()
                    print "speed: " + str(garage[chosen_car].speed)
                    response = raw_input("what do you want to do? \n" \
                        "(a)ccelerate \n" \
                        "(b)rake \n" \
                        "(t)urbo switch \n"
                        "(r)eturn to garage \n"
                        "(s)tatus")
                elif response == "b":
                    garage[chosen_car].brake()
                    print "speed: " + str(garage[chosen_car].speed)
                    response = raw_input("what do you want to do? \n" \
                        "(a)ccelerate \n" \
                        "(b)rake \n" \
                        "(t)urbo switch \n"
                        "(r)eturn to garage \n"
                        "(s)tatus")
                elif response == "t":
                    garage[chosen_car].turbo_switch()
                    print "turbo: " + str(garage[chosen_car].turbo)
                    response = raw_input("what do you want to do? \n" \
                        "(a)ccelerate \n" \
                        "(b)rake \n" \
                        "(t)urbo switch \n"
                        "(r)eturn to garage \n"
                        "(s)tatus")
                elif response == "r":
                    "back to garage"
                    driving = False
                    make_car()

                elif response == "s":
                    garage[chosen_car].status()
                    driving = False
                    drive()
        else:
            print "that's not in the garage"
            print garage
            drive()
    else:
        print "you don't have any cars yet"
        make_car()
make_car()

