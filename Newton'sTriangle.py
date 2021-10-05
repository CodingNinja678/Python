k = 1
i = 1
n = int(input('Enter number of rows : '))
while i <= n:
    j = 1
    while j <= i:
        print("{:3d}".format(k), end=" ")
        j += 1
        k += 1
    print()
    i =i+ 1
