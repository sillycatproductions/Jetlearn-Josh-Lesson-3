def factorial(n):
    #base condition
    if n == 1 or n == 0:
        return 1
    #recursive
    else:
        return n * factorial(n-1)
    
n = int(input('Enter a Number: '))
print('Factorial of', n,'is:',factorial(n))

    