import sys
from collections import deque
n = int(sys.stdin.readline())

#1
'''
def f_pop(l):                       # 제일 위 숫자 버리기
    return(l[1:])

def b_move(l):                      # 뒤로 옮기기
    return(l[1:]+l[0])

lt = []
for i in range(1,n+1):              # 1~n 숫자
    lt.append(str(i))

s = "".join(lt)

while 1:
    s = f_pop(s)
    s = b_move(s)
    
    if len(s) == 1:
        print(s)
        break
    
'''

#2
de = deque()
for i in range(1,n+1):              # 덱 구현
    de.append(i)

while len(de) > 1:
    de.popleft()                    # 맨 앞 떼고
    x = de.popleft()                # 앞에꺼 떼서
    de.append(x)                    # 맨 뒤 붙이고
print(*de)
