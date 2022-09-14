def d(n) :
    x = list(map(int,str(n)))

    # 각 자리 숫자의 합
    sum = 0
    for i in range(len(x)):
        sum += x[i]

    return n + sum

n = 1
arr = []
while n <= 10000 :
    dn = d(n)
    arr.append(dn)
    n += 1

ans = []
for i in range(1,10001) :
    if i not in arr:
        ans.append(i)

for x in ans:
    print(x)

