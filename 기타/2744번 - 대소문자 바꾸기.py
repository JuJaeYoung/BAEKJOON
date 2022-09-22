x = input()
#1
'''
lt = []
y = ''

for i in range(len(x)) :
    lt.append(x[i])

for j in range(len(lt)) :
    if lt[j] == lt[j].upper() :
        lt[j] = lt[j].lower()
    else :
        lt[j] = lt[j].upper()

for k in range(len(lt)) :
    y += lt[k]

print(y)
'''
#2
print(x.swapcase())
