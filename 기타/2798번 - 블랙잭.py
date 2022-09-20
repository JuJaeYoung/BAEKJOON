import sys
N,M = map(int,sys.stdin.readline().split())
x = list(map(int,input().split()))
l = []
lt = []

for i in range(len(x)-2) :               
    for j in range(i+1,len(x)-1) :        
        for k in range(j+1,len(x)) :
            l.append(x[i]+x[j]+x[k])


for a in l :
    if M - a >= 0 :
        lt.append(M-a)

print(M - min(lt))
