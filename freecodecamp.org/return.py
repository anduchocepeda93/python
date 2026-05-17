def cube(num):
    return num*num*num

result = cube(3)
print(result)    

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

result1 = factorial(4)
print(result1)  