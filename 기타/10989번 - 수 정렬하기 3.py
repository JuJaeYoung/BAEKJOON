import sys

N = int(sys.stdin.readline())
x = [0] * 10001

for i in range(N) :
    data = int(sys.stdin.readline())
    x[data] += 1

for i in range(10001) :
    if x[i] != 0 :
        for j in range(x[i]) :
            print(i)

