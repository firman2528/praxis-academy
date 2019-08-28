shopping_list = ['apple', 'manggo', 'carrot', 'banana']
print('I have ', len(shopping_list), 'items to purchase')

print('These items are: ', end=' ')

for item in shopping_list :
    print(item, end=' ')

print('\nI also have to buy rice.')
shopping_list.append('rice')
print('Now my shopping list is :', shopping_list)

print('I will sort my list now')
shopping_list.sort()
print('My shopping list is ', shopping_list)

print('The first item i want to buy is', shopping_list[0])
olditem = shopping_list[0]
del shopping_list[0]

print('I want to buy', olditem)
print('My shopping list now is ', shopping_list)