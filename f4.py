def onmywaytowork():
    task = int(input("What time is it?"))
    if task > 8:
        print("Oh no!  You're running late!")
    elif task < 8:
        print("You may have a little bit of time")
    else:
        print("Are you right on time?")

onmywaytowork()