earbuds = ("Airpods", "Samsung buds", "Beats budz")
headphones = ("Beats Headphones", "Sony Sports", "Skullcandy")

sounds = (earbuds,headphones)
earphones = (earbuds)*3
print(sounds)
print(earphones)

if earphones[0:3] == earbuds:
    print("hey earphones and earbuds are the same tuple! ")

setearphones = set(earphones)
setearbuds = set(earbuds)

if setearphones == setearbuds:
    del setearphones

try:
    setearphones
except:
    print("setearphones has been eliminated for redundency")