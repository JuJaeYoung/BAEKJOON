import sys
n = int(sys.stdin.readline())
x = {}
for i in range(n):
    word = input()
    length = len(word)
    x[word] = length

y = sorted(x.items(),key=lambda z:(z[1],z[0]))
for k,v in y:
    print(k)
