M = int(input())
N = int(input())
lt = range(M,N+1)               # M이상 N이하

l = []
sm = 0

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

if l == [] :
    print(-1)
else :
    for j in l :
        sm += j

    print(sm)
    print(min(l))
        
