zoo=('python', 'elephant', 'penguin')
print("Number of zoo", len(zoo))

new_zoo = 'monkey', 'camel', zoo

print('number of cages in new zoo ', len(new_zoo))

print('All animals in new zoo are ', new_zoo)

print('Animal brought from new zoo are', new_zoo[2])
print('last animal brought from new zoo are ', new_zoo[2][2])

print('Number of animals in new zoo is ', len(new_zoo)-1+len(new_zoo[2]))