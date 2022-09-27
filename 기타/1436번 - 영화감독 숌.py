'''
666 1666 2666 3666 4666 5666
6660 6661 6662 6663 6664 6665 6666 6667 6667 6669
7666 8666 9666 10666
'''

N = int(input())
six = 666
cnt = 0
while 1 :
    if '666' in str(six) :
        cnt += 1
        if cnt == N :
            print(six)
            break
    
    six += 1
