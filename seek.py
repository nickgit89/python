from asyncore import read


myFile=open("jelly.txt", "w")
myFile.write("This is only a test, but I like peanut butter and Jelly.")

myFile.close()

myFile= open("jelly.txt", "a")
myFile.write("You didn't think I was done, did you????")

myFile.close()

myFile= open("jelly.txt", "r")
print("Reading..." + myFile.read(10))

myFile.seek(15)

print("Reading again" + myFile.read(10))

print("Reading a line:" +myFile.readline())