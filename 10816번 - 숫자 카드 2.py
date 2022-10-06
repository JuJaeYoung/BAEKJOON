import sys
n = int(sys.stdin.readline())
nlt = list(sys.stdin.readline().split())
ndic = {}

for x in nlt:
    if x in ndic:
        ndic[x] += 1
    else:
        ndic[x] = 1

m = int(sys.stdin.readline())
mlt = list(sys.stdin.readline().split())
mcnt = []

for x in mlt:
    if x in ndic:
        mcnt.append(ndic[x])
    else:
        mcnt.append(0)
        
'''                                # count 쓰면 시간 초과
cnt = []
for x in mlt:
    cnt.append(nlt.count(x))
'''
print(*mcnt)


    
