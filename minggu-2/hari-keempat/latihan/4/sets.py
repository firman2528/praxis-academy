# creating two sets
set1 = set()
set2 = set()

# adding elements to set1
for i in range(1,6) :
    set1.add(i)


# adding elements to set2
for i in range(3,8) :
    set2.add(i)

print("Set1 =", set1)
print("Set2 = ", set2)
print("\n")

# Union of set1 and set2
set3 = set1 | set2 # atau pakai set1.union(set2)
print("Union set1 & set2 : set3 =", set3)

# Intersection of set1 and set2
set4 = set1 & set2 # atau pakai set1x.intersection(set2)
print("Intersection of set1 $ set2 : set4 = ", set4)

#checking relation between set3 and set4
if set3 > set4 : # atau pakai set3.isupperset(set4)
    print("Set3 is upperset of set4")
elif set3 < set4 : # set3x.issubset(set4)
    print("Set3 is subset of set4")
else : # set3 == set4
    print("Set3 is same as set4")

# displaying relation between set4 and set3
if set4 < set3 : # set4.issubset(set3)
    print("set4 is subset of set3")
    print("\n")

# difference between set3 and set4
set5 = set3 - set4
print("element in set3 and not in set4 = ", set5)
print("\n")

# check if set4 and set5 are disjoint sets
if (set4.isdisjoint(set5)) :
    print("set4 and set5 have nothing in common\n")

#Removing all the value of set5
set5.clear()

print("After applying clear of sets set5 :")
print("Set5 = ", set5)