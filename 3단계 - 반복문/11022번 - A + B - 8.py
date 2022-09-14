import sys

T = int(input())

for i in range(1,T+1):
    a,b = map(int,sys.stdin.readline().split())
    sum1 = 'Case #{}: {} + {} = {}'.format(i, a, b, a+b)
    print(sum1)

