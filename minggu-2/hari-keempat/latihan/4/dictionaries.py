d = {}

# add a key - value pair to dictionary
d['xyz'] = 123
d['abc'] = 345

# print the whole dictionary
print(d)

#print only the keys
print(d.keys())

#print only value
print(d.values())

#iterate over the dictionary
for i in d :
    print("{} {}".format(i,d[i]))

# another method of iteration 
# kalau mau pakai index musti pakai enumerate
for index, value in enumerate(d) :
    print(index, value, d[value])

#check if key exist 23. python data structure -
print('xyz' in d)

#deflete the key-value pair
del d['xyz']

#check again 
print("xyz" in d)