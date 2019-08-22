class SchoolMember :
    def __init__(self, name, age) :
        self.nama = name
        self.usia = age
        print("Initializing Schoolmember {}".format(self.nama))

    def tell(self) :
        print("Name {} Age {}".format(self.nama, self.usia, end=" "))


class Teacher(SchoolMember) :
    # Represent a teacher 
    def __init__(self, name, age, sallary) :
        SchoolMember.__init__(self, name, age)
        self.gaji = sallary
        print("Initializing Teacher {}".format(self.nama))

    def tell(self) :
        SchoolMember.tell(self)
        print("Sallary : {:d}".format(self.gaji))

class Student(SchoolMember) :
    # Represent a student 
    def __init__(self, name, age, mark) :
        SchoolMember.__init__(self, name, age) 
        self.marks = mark
        print("Initializing {}".format(self.nama))

    def tell(self) :
        SchoolMember.tell(self)
        print("Marks : {}".format(self.marks))

t = Teacher("Firman", 30, 20000000)
s = Student("Cacu", 11,100)
print()

member = [t,s]
for n in member :
    n.tell()
    