N = int(input())
count = 0                               # 그룹 단어 카운트

for i in range(N) :
    x = input()                         # N개만큼 단어 입력받기

    if len(x) == 1:                     # 1자리 문자열은 그룹단어.
        count += 1
    else : 
        for j in range(len(x)-1) :      # j 와 j+1 가 다른데 j+2 이후에서 같은것이 나올 때
            if x[j] == x[j+1] :         # 같은 문자로 이루어진 경우
                if j == len(x) - 2 :
                    count += 1
                    break
                else :
                    continue
            
            elif x[j] != x[j+1] and x.rfind(x[j]) > j+1 :
                break
            elif x[j] != x[j+1] and j == len(x) - 2 :
                count += 1
            
            

print(count)
