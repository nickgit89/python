from configparser import SafeConfigParser


character =input("Which character of Harry Potter would you like to know about?")
if character == "Harry Potter":
    print("Harry Potter is a member of Gryffindor.")
elif character == "Hermoine":
    print("Hermoine is a skilled member of Gryffindor")
elif character == "Severus Snape":
    print("Severus loved Lilly very much")
elif character == "Ron Weasley":
    print("Ron was Harry's best friend")
else:
    print("I do not have information on that character.")