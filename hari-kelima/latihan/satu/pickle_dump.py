import pickle
import io

class SimpleObject(object) :
    def __init__(self, name) :
        self.name = name
        l = list(name)
        l.reverse
        self.name_backwards = ''.join(l)
        return
    
data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('cPickle'))
data.append(SimpleObject(last))

# simulate a file string with StringIO
out_s = io.StringIO()

# Write to the string
for o in data :
    print('Writing : {} {}'.format(o.name, o.name_backwards))
    pickle.dump(o, out_s)
    out_s.flush()