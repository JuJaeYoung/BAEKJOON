n = int(input())
a = 0
i = 1
while True :
    if i == 1 :
        if n == 1 :                    # 1 출력
            print(i)
            break

        elif n >= 2 and n < 2 + 6 * i :
            print(i+1)                  # 2 출력
            break

        else :
            a = 2 + 6 * i
            i += 1
    else :
        if n >= a and n < a + 6 * i :
            print(i + 1)
            break
        else :
            a = a + 6 * i
            i += 1
