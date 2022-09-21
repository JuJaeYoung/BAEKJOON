import sys
r = 31
M = 1234567891
L = int(sys.stdin.readline())
x = sys.stdin.readline().lower()
s = 0

l = []
for i in x :
    l.append(ord(i)-96)

for j in range(L) :
    s += l[j] * (r ** j)
    
print(s % M)
