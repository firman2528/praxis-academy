
class Engine(object) :
    def __init__(self) :
        self.revs_per_minute = 0

    def turnon(self) :
        self.revs_per_minute = 2000

    def turnoff(self) :
        self.revs_per_minute = 0

    