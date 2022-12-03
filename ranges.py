listofpeople = range(25)

print(list(listofpeople))

for x in list(listofpeople):
    print(f"The person {x} is part of the list")


winners = range(2, 25, 10)

for y in list(winners):
    print(f"Person {y} is one of the blessed winners")