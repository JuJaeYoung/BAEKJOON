S = input()
x = 'abcdefghijklmnopqrstuvwxyz'            # a~z 리스트
location = []   # a~z 위치 리스트
for xi in x:
    location.append(S.find(xi))

print(*location)
