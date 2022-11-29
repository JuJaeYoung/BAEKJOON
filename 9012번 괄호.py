import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    VPS = sys.stdin.readline().strip()

    stack = []

    for paren in VPS:
        if paren == '(':            # '('이면 담고
            stack.append(paren)
        else:                       # ')'이면
            if len(stack):          # 길이가 0이 아니면
                stack.pop()         # 지우고
            else:                   # 길이가 0이면
                print('NO')         # 더이상 지울게 없으니 짝을 이루지 못했다는 의미.
                break
    else:
        if stack:
            print('NO')

        else:
            print('YES')
