x = eval(input("Please type in number of factorial you would like to see: "))

def factorial(a):
    if(a <= 1): 
        return a
    return a * factorial(a-1)

print("The factorial of " + str(x) + " is " + str(factorial(x)))