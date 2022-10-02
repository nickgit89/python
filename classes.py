class Hurricane():
    def __init__(self, name, wind, rain, damage):
        self.name = name
        self.wind = wind
        self.rain = rain
        self.damage = damage


    def createdamage(self):
        if wind > 130:
            print("The wind created damage.")
        else:
            print("It is possible it created damage.")


Ian = Hurricane("ian", 155, "lots", "catastrophic")


    