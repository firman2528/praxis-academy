sum(i*i for i in range(10)) # sum of squares

xvec=[10,20,30]

yvec = [7,5,3]

sum(x*y for x,y in zip(xvec, yvec))

from math import pi, sin
sin_table = {x : sin(x*pi/180) for x in range(0,91)}

unik_words = set(word for line in page  for word in line.split())

valedoctrian = max((student.gpa, student.name) for student in graduates)

data = 'golf'

list(data[i] for i in range(len(data)-1, -1, -1))