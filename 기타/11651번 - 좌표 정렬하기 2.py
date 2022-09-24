N = int(input())
lt = []

for i in range(N) :
    x,y = map(int,input().split())            # 점 입력
    lt.append([y,x])                          # (y,x) 리스트

lt.sort()

for j in range(N) :
    print(lt[j][1],lt[j][0])
