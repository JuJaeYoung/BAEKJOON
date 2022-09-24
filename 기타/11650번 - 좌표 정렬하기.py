N = int(input())
lt = []

for i in range(N) :
    lt.append(list(map(int,input().split())))            # 점 입력

lt.sort()

for j in range(N) :
    print(*lt[j])
