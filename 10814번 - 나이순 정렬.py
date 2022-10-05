import sys

n = int(sys.stdin.readline())

x = []
for i in range(n):                          # 리스트 만들기
    age, name = sys.stdin.readline().split()
    age = int(age)
    x.append((age,name))

x.sort(key=lambda y:y[0])

for i in x:
    print(i[0],i[1])


