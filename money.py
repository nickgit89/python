typesofmoney = ["dollars", "dolars", "pesos", "yen"]

for typeofmoney in typesofmoney:
    if typeofmoney == "pesos":
        print(typeofmoney.upper())
    if typeofmoney == "dolars":
        print(typeofmoney.title())
    else:
         print(typeofmoney.lower())

governments = {"democracy": "freedom", "dictatorship": "control"}

for government in governments:
    print(f"{government.title()} is a type of government")


soccerteams = ["liverpool", "wrexham", "FC"]

print(soccerteams[1])

message = f"I'm watching a show about {soccerteams[1].title()}"

print(message)

soccerteams.append('MadridFC')

print(soccerteams[3].title())

soccerteams.insert(1, "mexico City")

print(f"{soccerteams[1].title()} is the soccer team closest to me here in the United States")