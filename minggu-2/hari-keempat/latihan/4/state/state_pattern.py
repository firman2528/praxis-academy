class ComputerState(object) :
    name = "state"
    allowed = []

    def switch(self, state) :
        if state.name in self.allowed :
            print ("Current :", self , " => switched to a new state ", state.name)
            self.__class__ = state
        else :
            print("current :", self," => switching to sate ", state.name," not possible")

    def __str__(self) :
        return self.name


class Off(ComputerState) :
    name = "Off"
    allowed = ["On"]

class On (ComputerState) :
    name = "On"
    allowed = ["Off", "Suspend", "Hibernate"]

class Suspend(ComputerState) :
    name="Suspend"
    allowed=["On"]

class Hibernate(ComputerState) :
    name = "Hibernate"
    allowed=["On"]

class Computer(object) :
    # A class representing computer
    def __init__(self, model="HP") :
        self.model = model
        # state the computer -- default OFF
        self.state = Off()

    
    def change(self, state) :
        self.state.switch(state)

    
if __name__ == "__main__" :
    comp = Computer()
    comp.change(On)
    comp.change(Off) 
    comp.change(On) 
    comp.change(Suspend)
    comp.change(Hibernate)
    comp.change(On)
    comp.change(Off)