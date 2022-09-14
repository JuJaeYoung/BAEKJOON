a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
a5 = int(input())
a6 = int(input())
a7 = int(input())
a8 = int(input())
a9 = int(input())
a10 = int(input())

x = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
for i in range(10):
    x[i] = x[i] % 42
    
y = []
for ai in x:
    if ai in y:
        continue
    else:
        y.append(ai)

count = 0
for n in y:
    count += 1

print(count)
