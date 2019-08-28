class Robot :
    poppulation = 0
    
    def __init__(self, name) :
        self.nama = name
        print("Initializing {}".format(self.nama))

        Robot.poppulation += 1

    def die(self) :
        print("{} is being destroyed".format(self.nama))

        Robot.poppulation -=1

        if Robot.poppulation == 0 :
            print("{} was the last one".format(self.nama))
        else :
            print("There are still {:d} robots working".format(Robot.poppulation))

    
    def say_hi(self) :
        print("Greeting my master call me {}".format(self.nama))

    # method ini belong to class not object
    @classmethod
    def how_many(cls) :
        # print the current population
        print("We have {:d} robots".format(Robot.poppulation))

# droid = Robot("R2-D2")

# droid.say_hi()
# #bisa juga 
# # self.__class__.poppulation
# # atau pakai ini
# Robot.how_many()

# droid2 = Robot("C-3PO")
# droid2.say_hi()
# Robot.how_many()

# print("\nRobots can do some work here")

# print("\nRobot have finished their work now")

# droid.die()
# droid2.die()
# Robot.how_many
