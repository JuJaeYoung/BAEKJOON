lst = []
for i in range(28) :
    lst.append(int(input()))

i = 1
while i != 31 :
    try :
        if lst.index(i) >= 0 :
            i += 1
            continue
    except :
        print(i)
        i += 1
        continue
    
