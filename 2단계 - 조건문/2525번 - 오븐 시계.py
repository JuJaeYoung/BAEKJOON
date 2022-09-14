a,b = input().split()
c = input()
a = int(a)
b = int(b)
c = int(c)
if (c//60 >= 1):
    d = c - c//60 * 60
    if (b + d >= 60):
        if (a+c//60 >= 23):
            print(a+c//60-23,b+d-60)
        else:
            if (b + d >= 120):
                print(a+2+c//60,b+d-60)
            else:
                print(a+1+c//60,b+d-60)
    else:
        if (a+c//60 >= 24):
            print(a+c//60-24,b+d)
        else:
            print(a+c//60,b+d)    
else:
    if (b + c >= 60):
        if (a == 23):
            print(a-23,b+c-60)
        else:
            print(a+1,b+c-60)
    else:
        print(a,b+c)

