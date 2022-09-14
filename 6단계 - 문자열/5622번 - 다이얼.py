a = input()
a = a.upper()
sum = 0
lt = [['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]

for i in range(len(a)):
    for j in range(8):
        if a[i] in lt[j]:
            sum += j+3

print(sum)
