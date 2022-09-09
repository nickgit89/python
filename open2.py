myfile= open("textfile.txt", "a+")

for i in range(10):
    myfile.write("This is some new text\n")