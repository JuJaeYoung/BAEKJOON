x = list(map(int,input().split()))

sm = 0

for i in x :
    sm += i * i

print(sm % 10)
