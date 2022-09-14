c = int(input())

# 입력받은 점수들의 평균 구하기
def mean(n, x):
    su_m = 0
    for i in range(n):
        su_m += x[i]         # 점수 합
    mean = su_m / n

    return mean

for j in range(c):
    a = list(map(int,input().split()))
    n = a[0]
    score = a[1:]

    me = mean(n,score)

# 평균과 비교
    count = 0
    for x in score:
        if x > me:
            count += 1
    
    print ("%.3f%%" % (round(count/n*100,3)))

# 초기화
    a = []

