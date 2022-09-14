def rev(num) :    # 뒤집는 함수
    x = []
    for i in range(len(num)) :
        x.append(num[i])
    x.reverse()
    return x

A,B = input().split()

a = ''.join(rev(A))
b = ''.join(rev(B))

a = int(a)
b = int(b)

if a > b :
    print(a)
elif a < b :
    print(b)
