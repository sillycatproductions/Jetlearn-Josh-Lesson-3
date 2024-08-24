def fibbonaci(n):
    #base case
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    #recursive
    else:
        return (fibbonaci(n-1) + fibbonaci(n - 2))

n = int(input('Enter a number: '))
for i in range(0,n):
    print(fibbonaci(i), end = ' ')