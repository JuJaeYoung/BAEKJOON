n = input()

while n != '0' :
    x = "".join(reversed(n))

    if n == x :
        print('yes')
    else :
        print('no')

    n = input()
