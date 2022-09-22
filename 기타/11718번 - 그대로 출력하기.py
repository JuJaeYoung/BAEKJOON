x = []
while 1 :
    try :
        a = input()
        if a == '' :
            break
        else :
            x.append(a)
    except :
        break

for i in x :
    print(i)
