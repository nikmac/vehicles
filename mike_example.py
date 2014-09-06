class Vehicle(object):
    def __init__(self, color, seats = 5):
        self.seats = seats
        self.speed = 0
        self.direction = 0
        self.color = color

    def accelerate(self, x):
        print self.speed, '-->',
        self.speed += max(0,x)
        print self.speed

    def brake(self, x):
        print self.speed, '-->',
        self.speed -= max(0,x)
        print self.speed

    def turn_left(self):
        print self.direction, '-->',
        self.direction -= 90
        print self.direction, 'degrees'

    def turn_right(self):
        print self.direction, '-->',
        self.direction += 90
        print self.direction, 'degrees'


class RadioMixin(object):
    def turn_radio_on(self):
        self.radio = 'on'
        print 'Radio is: ' + self.radio

    def turn_radio_off(self):
        self.radio = 'off'
        print 'Radio is: ' + self.radio

    def change_station(self, station):
        self.radio = 'on'
        self.radio_station = station
        print self.radio_station

class ManualTrans(Vehicle, RadioMixin):
    def __init__(self, color):
        super(ManualTrans, self).__init__(color)
        self.clutch_in = False

    def engage_clutch(self):
        self.clutch_in = True

    def disengage_clutch(self):
        self.clutch_in = False

    def brake(self, x):
        self.engage_clutch()
        super(ManualTrans, self).brake(x)

class ManualCar(ManualTrans):
    def __init__(self, color):
        super(ManualCar, self).__init__(color)
        self.color = color
        self.speed = 10
        self.top_speed = 165

    def accelerate(self, x):
        super(ManualCar, self).accelerate(x)

    def engage_clutch(self):
        super(ManualCar, self).engage_clutch()
        # self.clutch_in = 'Not engaged'


class RaceCar(ManualCar):
    def __init__(self):
        super(RaceCar, self).__init__('Red')
        self.speed = 0

    def accelerate(self, x):
        super(RaceCar, self).accelerate(x)


class StreetCar(ManualCar):
    def __init__(self):
        super(StreetCar, self).__init__('Yellow')


class Motorbike(ManualTrans):
    def __init__(self, color):
        super(Motorbike, self).__init__(color)


class AutoTrans(Vehicle, RadioMixin):
    def __init__(self, color):
        super(AutoTrans, self).__init__(color)

class AutoCar(AutoTrans):
    def __init__(self):
        super(AutoCar, self).__init__('Silver')


class Boat(AutoTrans):
    def __init__(self):
        super(Boat, self).__init__('White')
        self.float_well = True


def drive_vehicle(name , vehicle):
    while True:
        print 'Your vehicle, {}, is going {} mph, {} degrees from north, clockwise.'.format(name, vehicle.speed, vehicle.direction)
        action = raw_input('What do you want to do? \n\tTurn (L)eft\n\tTurn (R)ight\n\tSpeed (U)p\n\tSpeed (D)own\n\tOr (Q)uit\n').lower()
        if action == 'q':
            break
        elif action == 'l':
            vehicle.turn_left()
        elif action == 'r':
            vehicle.turn_right()
        elif action == 'u':
            step = int(raw_input("How much do you want to speed up? "))
            vehicle.accelerate(step)
        elif action == 'd':
            step = int(raw_input("How much do you want to slow down? "))
            vehicle.brake(step)
        else:
            print "Sorry I didn't understand. Please try again."
    return "Welcome back."


def vehicle_manager():
    garage = {}
    garage['1963 Mercury GT Sport Racer'] = RaceCar()
    garage['Chevrolet Corvette ZR1'] = StreetCar()
    garage['Suzuki Hayabusa'] = Motorbike('Jet Black')
    garage['2010 Honda Civic'] = AutoCar()
    garage['Rowboat'] = Boat()

    for x in garage:
        # garage[x].turn_radio_on()
        # print x, garage[x].color, garage[x].radio
        print '#'*80
        print x
        print drive_vehicle(x, garage[x])

vehicle_manager()

#########################Testing###############################

# my_racecar = RaceCar()
# my_streetcar = StreetCar()
# my_vehicle = Vehicle('pink')
#
# print my_vehicle.color
# my_vehicle.accelerate(5)
#
#
# my_racecar.accelerate(20)
#
#
# print my_streetcar.color
# print my_streetcar.clutch_in
#
#
# my_car = ManualCar('Black')
# print my_car
# print my_car.color, my_car.top_speed, 'My car has ' + str(my_car.seats) + ' seats.'
# my_car.accelerate(20)
# print my_car.clutch_in
# print my_car.engage_clutch()
# print my_car.clutch_in
