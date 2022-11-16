import os 

terminal= os.ctermid()

print(terminal)

os.chdir('/home')

cwd = os.getcwd()

print("Current working folder is:", cwd)

with open('test.txt', 'w') as W:
    W.write('I want you to create a document!')