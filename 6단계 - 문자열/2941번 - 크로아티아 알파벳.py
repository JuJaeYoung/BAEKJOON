x = input()
y = ['c=','c-','dz=','d-','lj','nj','s=','z=']
count = 0
ans = 0

for y1 in y :
    if y1 in x :
        z = x.split(y1)                 # 찾는 문자 없애기
        count += len(z) - 1             # 없앤 문자 갯수

ans = count + len(x) - count * 2
print(ans)
