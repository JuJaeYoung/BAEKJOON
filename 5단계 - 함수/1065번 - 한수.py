def h_100_10(n) :
    return n // 100 - (n // 10 - n // 100 * 10)

def h_10_1(n) :
    return (n // 10 - n // 100 * 10) - n % 10

n = int(input())


if n >= 1 and n < 100 :
    count = n
else:
    count = 99
    for x in range(100,n+1) :
        if h_100_10(x) == h_10_1(x) :
            count += 1

print(count)
