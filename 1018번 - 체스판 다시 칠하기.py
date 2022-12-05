import sys

n, m = map(int,sys.stdin.readline().split())

lst = []

for _ in range(n):
    lst.append(sys.stdin.readline().strip())



result = []

for i in range(n-7):    
    for j in range(m-7):
        C_W = 0
        C_B = 0
        
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k + l) % 2 == 0:
                    if lst[k][l] != 'W':
                        C_W += 1
                    if lst[k][l] != 'B':
                        C_B += 1
                else:
                    if lst[k][l] != 'B':
                        C_W += 1
                    if lst[k][l] != 'W':
                        C_B += 1                       
        

        result.append(C_W)
        result.append(C_B)
       

print(min(result))
