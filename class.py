from webbrowser import BackgroundBrowser


class hair:
    def __init__(self, color, length, texture):
        self.color = color
        self.length = length
        self.texture = texture
    
    def cuthair(self, str="clip, clip, clip"):
        print(str)

class myhair(hair):
    def __init__ (self, color, length, texture):
        self.color = color
        self.length = length
        self.texture = texture

hair = myhair("brown", "long", "straight")

print(hair.color)


class infraction:
    def __init__(self, type, fine, jailtime):
        self.type = type
        self.fine = fine
        self.jailtime = jailtime
    
felony = infraction("severe", 2000, "yes")

print(felony.type)

misdemeanor = infraction("less_serious", "500", "no")

print(misdemeanor.jailtime)


class fine:
    def __init__(self, type, money):
        self.type= type
        self.fine= fine
        self.money= money

    bigfine = fine("ticket", "50", "USD")

print(bigfine)