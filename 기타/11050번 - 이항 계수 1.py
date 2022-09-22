N,K = map(int,input().split())

def fac(n) :
    m = 1
    for i in range(n,0,-1) :
        m *= i
    return m

x = fac(N) / (fac(K)*fac(N-K))
print(int(x))
