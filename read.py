myfile= open("textfile.txt", "r")

if myfile.mode == 'r':
    #contents = myfile.read()
    #print(contents)


    fl = myfile.readlines()
    for x in fl:
        print(x)
