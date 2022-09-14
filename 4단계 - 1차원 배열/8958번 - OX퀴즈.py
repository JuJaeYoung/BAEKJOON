n = int(input())

# O 개수만큼 더하는 함수
def cycle(test):
    count = 0
    sum = 0
    for i in range(len(test)):
        if test[i] == "O":
            count += 1
            sum += count
        else:
            count = 0        

    return sum


for i in range(n):
    test = input()
    a = cycle(test)
    print(a)
