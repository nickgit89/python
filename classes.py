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


class Tornado():
    def __init__(self, warning, wind, shape):
        self.warning = warning
        self.wind = wind
        self.shape = shape

Cyclone = Tornado("unexpected", "strong", "circle")

print(Cyclone.wind)