myfile= open("textfile.txt", "r")

if myfile.mode == 'r':
    contents = myfile.read()
    print(contents)
