length = 12
astr = "<>"
for x in range(length):
    for y in range(length-x):
        print(" ", end = "")

    print(astr)
    astr += "<>"


    