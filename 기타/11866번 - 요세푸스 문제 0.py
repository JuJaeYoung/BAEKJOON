import sys
N, K = map(int,sys.stdin.readline().split())
a = K
x = []
lt = []
for i in range(1,N+1) :
    x.append(i)         # 1~N까지의 리스트  # ok


while x != [] :         # 빈 리스트가 아닐때까지
    while a > len(x) :
        a -= len(x)
    lt.append(x[a-1])
    x.remove(x[a-1])
    a += K-1

print('<',end="")
for i in lt :
    if i == lt[len(lt)-1] :
        print(i, end=">")
    else :
        print(i,end = ", ")
        
