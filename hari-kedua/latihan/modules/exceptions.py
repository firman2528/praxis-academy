class Eror(Exception) :
    pass

class InputError(Eror) :
    # Exception raised for errors in the input
    # Attributes : 
        # expression -- input expression in which the error occured
        # message -- explanation of the error

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error) :
    def 
    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
        