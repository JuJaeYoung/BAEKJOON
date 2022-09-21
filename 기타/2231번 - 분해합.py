import sys
N = input()

has_answer = False
start = max(1,int(N)-(len(N)*9))

for i in range(start, int(N)):
        x = str(i)
        sum = int(x)

        for j in range(len(x)) :
            sum += int(x[j])

        if sum == int(N):
            print(i)
            has_answer = True
            sys.exit(0)

if has_answer == False :
            print("0")
