
from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
l = deque()
for i in range(N) :
    deque_str = input().split()

    if deque_str[0] == 'push_front' :
        l.appendleft(deque_str[1])
    elif deque_str[0] == 'push_back' :
        l.append(deque_str[1])
    elif deque_str[0] == 'pop_front' :
        if l :
            print(l.popleft())
        else :
            print('-1')
    elif deque_str[0] == 'pop_back' :
        if l :
            print(l.pop())
        else :
            print('-1')
    elif deque_str[0] == 'size' :
        print(len(l))
    elif deque_str[0] == 'empty' :
        if l :
            print('0')
        else :
            print('1')
    elif deque_str[0] == 'front' :
        if l :
            print(l[0])
        else :
            print('-1')
    elif deque_str[0] == 'back' :
        if l :
            print(l[-1])
        else :
            print('-1')

'''
import sys
N = int(sys.stdin.readline())
l = []

def push_f(x, l) :                 # 맨 앞 x 넣기
    return l.insert(0,x)

def push_b(x, l) :                 # 맨 뒤 x 넣기
    return l.append(x)

def pop_f(l) :
    if l != [] :
        print(l[0])
        l.remove(l[0])
    else :
        print('-1')
    return l

def pop_b(l) :
    if l != [] :
        print(l[-1])
        l.remove(l[-1])
    else :
        print('-1')
    return l

def size(l) :
    print(len(l))

def empty(l) :
    if l == [] :
        print('1')
    else :
        print('0')

def front(l) :
    if l != [] :
        print(l[0])
    else :
        print('-1')

def back(l) :
    if l != [] :
        print(l[-1])
    else :
        print('-1')


for i in range(N) :
    A = list(sys.stdin.readline().split())
    if len(A) == 2 :
        x = int(A[1])
        if A[0] == 'push_front' :
            push_f(x, l)
        elif A[0] == 'push_back' :
            push_b(x, l)
    elif len(A) == 1 :
        if A[0] == 'pop_front' :
            l = pop_f(l)
        elif A[0] == 'pop_back' :
            l = pop_b(l)
        elif A[0] == 'size' :
            size(l)
        elif A[0] == 'empty' :
            empty(l)
        elif A[0] == 'front' :
            front(l)
        elif A[0] == 'back' :
            back(l)
'''
