ab = {
    'Swaroop' : 'swaroops@swaroop.com',
    'Larry' : 'larry@wall.org',
    'Matsumoto' : 'matz@matz.com',
    'Spammer' : 'spammer@spammer.com'
}



print('Swaroop address is', ab['Swaroop'])

del ab['Spammer']

print('\nThere are {} contact in the address-book\n'.format(len(ab)))

for name,address in ab.items() :
    print('Contact {} at {}'.format(name, address))

ab['Guido'] = 'guido@python.com'

if 'Guido' in ab :
    print('\nGuido address is ', ab['Guido'])


nama = ['firman', 'cacu', 'keya', 'cherry']
alamat = ['Bojong', 'Gede','Kabupaten','Bogor']


for nm, amt in zip(nama,alamat) :
    print('Nama : {} \nAlamat : {}'.format(nm,amt))