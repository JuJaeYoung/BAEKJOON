N,M = map(int,input().split())
A = []
for ni in range(N) :        # n개의 줄
    A.append(list(map(int,input().split())))

B = []
for ni in range(N) :        # n개의 줄
    B.append(list(map(int,input().split())))


for i in range(N) :
    AB = []
    for j in range(M) :
        AB.append( A[i][j] + B[i][j])
    print(*AB)


