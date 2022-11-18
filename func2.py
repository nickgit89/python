def flythekite():
    class kite:
        def __init__(self,color, fabric, price):
            self.color = color
            self.fabric = fabric
            self.price = price
    input("What type of kite do you want?")
    color = input("Please enter the color: ")
    fabric = input("Please enter the fabric: ")
    price = input("Please enter the price: ")
    yourkite = kite(color, fabric, price)
    print(f"Your {color} kite made of {fabric} is {price} dollars. Watch it fly away!")
    print(f"Your kite is located at memory space {yourkite}")
flythekite()


