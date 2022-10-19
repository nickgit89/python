File = open("names.txt", "w")


#w - write
# r - read
# r + = read and write
# a - append

print ("Name" + File.name)
print("Mode" + File.mode)

File.write("Nick : 200 \n John: 100")
File.close()

File = open("names.txt", "r")
print(f"Reading... {File.read()}")