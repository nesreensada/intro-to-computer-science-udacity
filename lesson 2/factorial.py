# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    
    x=n
    fact=1
    while x>=1:
        fact*=x
        x=x-1
    return fact    
    



print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720

