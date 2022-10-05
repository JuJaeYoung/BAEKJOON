# 파스칼 삼각형
'''
x층        1    1    1    1    1    1    1    1 
0층   1    2    3    4    5    6    7    8    9  
1층   1    3    6   10   15   21   28   36   45 
2층   1    4   10   20   35   56   84  120  165  
3층   1    5   15   35   70  126  210  330  495 
4층   1    6   21   56  126  252  462  792 1287 
5층   1    7   28   84  210  462  924

4층 4호 => 8C3 / 8C5
4층 3호 => 7C2 / 7C5
5층 5호 => 10C4 / 10C6
2층 7호 => 9C6 / 9C3
'''
# k층 n호 => (k+n) combination (n-1)

def fac(n) :
    m = 1
    for i in range(n,0,-1) :
        m *= i
    return m
    

T = int(input())

for _ in range(T):      # T번 반복
    k = int(input())
    n = int(input())
    x = fac(n+k) / (fac(n-1)*fac(k+1))
    print(int(x))


