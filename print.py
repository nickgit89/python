word = "programming is really cool"

vowels = ["a", "e", "i", "o", "u"]

vowelcount= 0 
for character in word:
    if character in vowels:
        vowelcount +=1

print("vowelcount is:", vowelcount)