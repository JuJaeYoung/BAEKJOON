n = int(input())
x = []
y = []
r = [0] * n


for _ in range(n) :
    a,b = list(map(int,input().split()))
    x.append(a)
    y.append(b)

for i in range(n) :
    cnt = 0
    for j in range(n) :
        if x[i] < x[j] and y[i] < y[j] :
            cnt += 1
    r[i] = cnt + 1


print(*r)


'''
5

55 185  4   2
58 183  3   3
88 186  1   1
60 175  2   4
46 155  5   5
'''
