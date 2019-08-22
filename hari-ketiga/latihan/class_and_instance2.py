class Dog :
    def __init__(self, name) :
        self.nama = name
        self.tricks=[]

    def add_trick(self, trick) :
        self.tricks.append(trick)

d = Dog("Buddy")
d.add_trick("Melompat")

e = Dog("bruno")
e.add_trick("Berlari")

print(d.tricks)
print(e.tricks)