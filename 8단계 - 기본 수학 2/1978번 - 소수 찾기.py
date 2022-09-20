N = int(input())
lt = list(map(int,input().split()))         # N개의 수

l = []

def cy(n) :
    x = 0
    b = ''
    if n != 1 :
        for i in range(2,n) :
            if n % i == 0 :             # 소수 X
                break
            else :                      # 소수일수도..
                x += 1
                continue    
        if x == n-2 :
            b = 'o'
        else :
            b = 'x'
    else :
        b = 'x'
    
    return b    

for a in lt :
    if cy(a) == 'o' :
        l.append(a)


print(len(l))
