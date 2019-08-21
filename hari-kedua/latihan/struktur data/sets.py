bri = set(['brazil', 'russia', 'india'])

'india' in bri

bric = bri.copy()
bric.add('china')

bric.issuperset(bri)

bri.remove('russia')

bri & bric