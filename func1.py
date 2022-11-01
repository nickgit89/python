def func1():
    print("I am a function.")


func1()
print(func1())
print(func1)


def func2(arg1, arg2):
    print (arg1," ", arg2)

def cube():
    x= int(input("Please put a number, so we can find it cubed:"))
    return x * x * x


func2(10, 30)
print(func2(10, 30))

def exponentofthree(value):
    return 3 ** value

print(exponentofthree(4))


list = [1,2,3,4]

def appendlist():
    number = int(input("Please put a number:"))
    list.append(number)

appendlist()

cube()

print(list)






        
