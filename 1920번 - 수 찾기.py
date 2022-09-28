N = int(input())
N_lt = set(input().split())

M = int(input())
M_lt = list(input().split())

for x in M_lt :
    if x in N_lt :
        print(1)
    else :
        print(0)
