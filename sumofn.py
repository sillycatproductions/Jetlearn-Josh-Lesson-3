def sum(n):
    #base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    #recursive
    else:
        return n + sum(n - 1)

n = int(input('Enter a Number: '))
print('The sum of', n,'is: ', sum(n))