mythic = {'type': 'game', 'source': 'show', 'age': 'medieval'}

mythic.update({'source':'video game'})

print(mythic)

#mythic.add({'subscription':'paid'})
print(mythic)

del mythic['type']
mythic.pop('age')
mythic['service']='Appletv'

print(mythic)
print(mythic['source'])