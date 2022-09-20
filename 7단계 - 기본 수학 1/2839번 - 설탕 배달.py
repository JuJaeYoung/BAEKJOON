N = int(input())

l = []


x5 = N // 5                     # x5 : 5로 나눈 몫

for i in range(x5 + 1) :
    a = (N - 5 * i)             # a : 5 부분 빼고 3 부분만 !
    if a % 3 == 0 :             # 3으로 나누어 떨어지면
        x = i + a // 3          # 횟수
        l.append(x)
    else :
        continue

if l == [] :                    # 리스트가 비었다면
    print(-1)
else :
    print(min(l))
    

