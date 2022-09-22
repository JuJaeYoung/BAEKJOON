x,y = map(int,input().split())

#최대공약수 구해서 두 수의 곱에서 나누면 최소공배수

i = min(x,y)
M = 0                                   # 최소공배수
m = 0                                   # 최대공약수

while 1 :
    if x % i == 0 and y % i == 0 :      # 최대공약수를 찾으면
        m = i
        break
    else :                              # 못찾으면 숫자 줄여서 찾아보기
        i -= 1

M = int((x * y) / m)
print(m)
print(M)
