# x 0 z 호

T = int(input())
for i in range(T) :
    H,W,N = map(int,input().split())

    if H > N :             
        x = N
        z = 1
        
    else :
        if N % H == 0 :     
            x = H
            z = N // H   
        else :
            z = N // H + 1
            x = N - (z - 1) * H

    print(f'{x*100+z}')
