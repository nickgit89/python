adict = dict(maple = "tree", pine = "evergreen", oak = "tree")
print(adict)

bdict = {"maple": "tree", "pine": "evergreen", "oak": "tree"}

zipdict = dict(zip(["maple", "pine", "oak"], ["tree", "evergreen", "tree"]))

zdict = dict({"maple": "tree", "pine": "evergreen", "oak": "tree"})

print(adict == bdict == zipdict == zdict)

trees = {}
trees["willow"] = "tree"
trees["palm"] = "tropical"
trees["apple"] = "fruit"

print(trees)

del trees["apple"]

print("palm" in trees)