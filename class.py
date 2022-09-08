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
