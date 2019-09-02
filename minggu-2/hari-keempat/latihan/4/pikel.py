import pickle

# Here's an example dict
grades = {'Alice' : 89, 'Bob' : 72, 'Charles' : 87}

#use dumps to convert the object to a serialized string
serial_grades = pickle.dumps(grades)
print("convert json ke serialized data menggunakan pickle.dumps()")
print(serial_grades)

# use loads to de-serialize an object
print("\n")
received_grades = pickle.loads(serial_grades)
print("Merubah serialized data menjadi json kembali menggunakan pickle.loads()")
print(received_grades)