typesofmovies = ['action', 'comedy']

typesofmovies.append('romance')

typesofmovies2 = typesofmovies.copy()

typesofmovies.clear()

print(typesofmovies)
print(typesofmovies2)

typesofmovies2.reverse()

print(typesofmovies2)

action = typesofmovies2.pop()
print(action)

typesofmovies2.remove('comedy')
typesofmovies2.insert(2, 'comedy')
