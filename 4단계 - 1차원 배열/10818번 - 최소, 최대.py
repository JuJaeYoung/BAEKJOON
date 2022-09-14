import sys

N = int(input())
a = list(map(int,sys.stdin.readline().split()))
max_a = a[0]
min_a = a[0]

for x in a:
    if x > max_a:
        max_a = x
    elif x < min_a:
        min_a = x

b = [min_a,max_a]
print(*b)
