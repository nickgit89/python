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