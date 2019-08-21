shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

print('Item in index 0 is', shoplist[0])
print('Item in index 1 is', shoplist[1])
print('Item in index 2 is', shoplist[2])
print('Item in index 3 is', shoplist[3])
print('Item in index -1 is', shoplist[-1])
print('Item in index -2 is', shoplist[-2])
print('Item in index 0 is', shoplist[0])

# slicing on a list 
print('Item 1 to 3 is ', shoplist[1:3])
print('Item 2 to end is ', shoplist[2:])
print('Item 1 to -1 is ', shoplist[1:-1])
print('Item start to end is ', shoplist[:])

# slicing on a string
print('Character 1 to 3 is ', name[1:3])
print('Character 2 to end is', name[2:])
print('Character 1 to -1 is ', name[1:-1])
print('Character start to end is ', name[:])


shoplist[::1]
shoplist[::2]
shoplist[::3]
shoplist[::-1]

