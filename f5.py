#People and favorite drinks

people = ["Nick", "Joe", "Dwight", "Helen"]
drinks = ["coffee", "Lemonade", "Pop", "Soda"]

for position, person in enumerate(people):
    drink = drinks[position]
    print(person, drink)


#people and their favorite foods:

foods = ["chipotle", "pizza", "salad", "hamburger"]

for person, food in zip(people, foods):
    print(person, food)