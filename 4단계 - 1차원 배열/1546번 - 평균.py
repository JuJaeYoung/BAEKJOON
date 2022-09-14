N = int(input())                                # 과목수
lt = list(map(int,input().split()))             # 성적

M = lt[0]
for x in lt:                                    # 최댓값 찾기
    if x > M:
        M = x
        
sum = 0
for x in lt:
        x = x / M * 100
        sum += x

print(sum/N)
