T = int(input())

for i in range(T) :         # 반복시행
    R,S = input().split()
    x = []
    for j in range(len(S)):
        x.append(S[j]*int(R))
    y = ''.join(x)
    print(y)
