import string


Loveisland = "show in Great Britain"
temptationisland ="show on USA Network"
numberofshows = 67

print(string.ascii_letters)


newLoveisland = "".join(x for x in Loveisland if x in string.ascii_letters)

print(newLoveisland)
