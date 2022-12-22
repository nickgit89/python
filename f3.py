from collections import namedtuple

Car = namedtuple('cars', ['sedan', 'convertible'])

car = Car('lid', 'no lid')

print(Car.sedan)


d = {}

d['points'] = d.get('points', 0) + 1

print(d)

d = {'points': 22}

print(d)


