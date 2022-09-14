a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
a5 = int(input())
a6 = int(input())
a7 = int(input())
a8 = int(input())
a9 = int(input())
count = 0

b = [a1,a2,a3,a4,a5,a6,a7,a8,a9]
max_b = b[0]

for i in range(9):
    if b[i] > max_b:
        max_b = b[i]
        count = i

print(max_b)
print(count+1)
