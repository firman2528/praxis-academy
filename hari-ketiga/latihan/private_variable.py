class Mapping :
    def __init__(self, iterable) :
        self.item_list = []
        self.__update(iterable)

    def update(self, iterable) :
        for item in iterable :
            self.item_list.append(item)
    
    __update = update

class MappingSubclass(Mapping) :
    def update(self, key, value) :
        for item in zip(key, value) :
            self.item_list.append(item)