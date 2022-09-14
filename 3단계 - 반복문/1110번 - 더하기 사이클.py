N = int(input())
count = 0
a = N

while True:
        
    if a < 10:
        a1 = a
        a3 = a 
    else :
        a1 = a - (a // 10) * 10                 # 주어진 수의 오른쪽 자리
        a2 = a // 10 + (a - (a // 10) * 10)       # 합의 오른쪽 자리
        a3 = a2 - (a2 // 10) * 10 
    count += 1
    a = a1 * 10 + a3

    if a == N:
        break
    
print(count)
