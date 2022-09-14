# 1  2  6  7 15 16
# 3  5  8  14 17
# 4  9  13 18
# 10 12 19
# 11 20
# 21

x = int(input())                    # 숫자 입력
i = 2
a = 1
sm = 0
while True :                        # 입력값이 어느 구간에 속하는지..
    if x <= a :
        n = i - 1                   # n 번째 구간에 속함. 더해서 n+1
        break
    else :
        a += i
        i += 1

for j in range(1,n) :
    sm += j

x = x - sm

if n % 2 == 0 :                     # 짝수번째
    print(f'{x}/{n+1-x}')
else :                              # 홀수번째
    print(f'{n+1-x}/{x}')
