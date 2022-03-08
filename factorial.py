#compute the factorial of a value
#return 1 if value is 0 or 1
def factorial(value):
    if value==0:
        return 1
    else:
        return value*factorial(value-1)




print(factorial(5))