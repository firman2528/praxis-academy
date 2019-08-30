
class _DashboardLight(object) :
    def __init__(self, is_on = False) :
        self.is_on = is_on

    def __str__(self) :
        return self.__class__.__name__

    @property
    def is_on(self) :
        return self.is_on

    @is_on.setter
    def is_on(self,status) :
        self.is_on =status

    def status_check(self) :
        if self.is_on :
            print("{} ON", self)
        else :
            print("{} OFF", self)

        