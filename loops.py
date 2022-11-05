counting = 10
while counting > 0:
    print( """ ^ 
             <    >""" * counting)
    counting -=1



for x in range(0, 10):
    print( """ ^
             <    >""" * x)


Expressions = ["Hello there!", "Whats your name", "How is it going"]

for expression in Expressions:
    print(expression)

for x in range (0, 20):
    if x % 2 == 0:
        continue
    if x == 13:
        break
        print("In IF:", x)
    
    print(x)