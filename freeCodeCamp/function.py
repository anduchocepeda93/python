def say_hi():
    print("Hi!")
def say_bye():
    print("Bye!")
def math():
    num1 = 2
    num2 = -3
    total = num1 + num2
    print(total)
say_hi()
say_bye()
math()

def say_hi(name):
    print(f"Hi {name}!")
def say_bye(name):
    print(f"Bye {name}!")
def math(num1,num2):
    total = num1 + num2
    print(total)    
say_hi("Alice")
say_bye("Bob")
math(2, -3)