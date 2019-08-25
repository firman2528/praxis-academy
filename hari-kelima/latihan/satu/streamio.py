import pickle 
from io import BytesIO

class SimpleObject(object) :
    def __init__(self, name) :
        self.name = name
        l = list(name)
        l.reverse()
        self.name_backwards= ''.join(l)
        return 
    
data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('cPickle'))
data.append(SimpleObject('last'))

out_s = BytesIO()

# write to the stream
for o in data :
    print('Writing {} {}'.format(o.name, o.name_backwards))
    pickle.dump(o, out_s)
    out_s.flush()
    
#setup a readable stream
in_s = BytesIO(out_s.getvalue())

# Read the data
while True :
    try :
        o = pickle.load(in_s)
    except EOFError :
        # print("Error")
        break
    else :
        print('Read {} {}'.format(o.name, o.name_backwards))