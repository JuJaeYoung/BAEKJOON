import sys

N = int(sys.stdin.readline())       # 홀수
x = []
y = [0] * 8001
for i in range(N) :
    a = int(sys.stdin.readline())   # 숫자 입력
    x.append(a)                     # 숫자 리스트
    y[a+4000] += 1                  # 0 입력 => 4000번에 저장
x.sort()

# 산술평균
add = 0
for i in range(N) :
    add += x[i]
print(int(round(add / N,0)))


# 중앙값
print(x[N//2])


# 최빈값
M_id = y.index(max(y))

if max(y) == 1 :
    if N != 1 :
        print(x[1])
    else :
        print(x[0])

else :
    for i in range(M_id + 1,8002) :
        if i != 8001 :
            if y[M_id] == y[i] :
                print(i - 4000)
                break
        elif i == 8001 :
            print(M_id - 4000)
            break


        

# 범위

print(max(x) - min(x))



        
