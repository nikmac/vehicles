from vehicle import *

def add_race_car():
    name = raw_input("What is the name of this racecar?")
    color = raw_input("What color do you want?")
    race_car = RaceCar(name, color)
    garage[name] = race_car


def add_street_car():
    name = raw_input("What is the name of this streetcar?")
    color = raw_input("What color do you want?")
    street_car = StreetCar(name, color)
    garage[name] = street_car

def add_motorbike():
    name = raw_input("What is the name of this motorbike?")
    color = raw_input("What color do you want?")
    motorbike = MotorBike(name, color)
    garage[name] = motorbike

def add_boat():
    name = raw_input("What is the name of this boat?")
    color = raw_input("What color do you want?")
    boat = Boat(name,color)
    garage[name] = boat

garage = {}
def buy_a_rig():
    print ""
    make_or_drive = raw_input("How can I help you? \n\t(M)ake a new rig \n\t(D)rive a rig I already made   ").lower()
    print ""
    if make_or_drive == "m":
        what_rig = raw_input("What do you want to make today? \n\t(R)acecar, \n\t(S)treetcar, \n\t(M)otorbike, \n\t(B)oat, \n\t(Q)nothing-just browsing  ").lower()
        if what_rig == "r":
            add_race_car()
            print "Great! I can make you an insane deal on this race car today.  Maybe you want to drive it first? "
            buy_a_rig()
        elif what_rig == "s":
            add_street_car()
            print "Great! I can make you an insane deal on this street car today.Maybe you want to drive it first?"
            buy_a_rig()
        elif what_rig == "m":
            add_motorbike()
            print "Great! I can make you an insane deal on this motorbike today.Maybe you want to drive it first?"
            buy_a_rig()
        elif what_rig == "b":
            add_boat()
            print "Great! I can make you a fairly ok deal on this boat,"
            print " if you're willing to wait while I go to lunch...Maybe you want to drive it first?"
            buy_a_rig()
        else:
            print "Uh...what are you talking about?"
            buy_a_rig()
    elif make_or_drive == "d":
        drive()
    else:
        print "Uh...what are you talking about?"
        buy_a_rig()


def drive():
    if len(garage) > 0:
        for rig in garage:
            print rig
        chosen_rig = raw_input("which rig do you want to test drive? ")
        if chosen_rig in garage:
            print ""
            print "I'll get the keys for  " + chosen_rig
            print ""
            while True:
                print 'Your {}, is going {} mph, {} degrees from north, clockwise.'.format(garage[chosen_rig], garage[chosen_rig].speed, garage[chosen_rig].direction)
                action = raw_input('What do you want to do? \n\tTurn (L)eft\n\tTurn (R)ight\n\tSpeed (U)p\n\tSpeed (D)own\n\tOr (Q)uit\n').lower()
                if action == 'q':
                    break
                elif action == 'l':
                    garage[chosen_rig].turn_left()
                elif action == 'r':
                    garage[chosen_rig].turn_right()
                elif action == 'u':
                    step = raw_input("How much do you want to speed up? ")
                    garage[chosen_rig].accelerate(int(step))
                elif action == 'd':
                    step = int(raw_input("How much do you want to slow down? "))
                    garage[chosen_rig].brake(step)
                else:
                    print "Sorry I didn't understand. Please try again."
            return "Welcome back."

        else:
                    print "that's not on the lot"
                    print garage
                    drive()
    else:
        print "That's great, but first I need to know\nmore about what you want to drive.  \nPlease make a rig first."
        buy_a_rig()

print ""
print ""
print "Hey there!  Welcome to the car lot."
print "We specialize in custom orders."
print "You should begin by making your dream vehicle."
print ""
buy_a_rig()