import sys
n = int(sys.stdin.readline())
l = []
def push(l,x):
    a,b = x.split()
    return l.append(int(b))

def size(l):
    print(len(l))

def empty(l):
    if l == []:
        print(1)
    else:
        print(0)

def top(l):
    if l != []:
        print(l[len(l)-1])
    else:
        print(-1)

for _ in range(n):
    x = sys.stdin.readline()
    
    if "push" in x:
        push(l,x)
    elif "pop" in x:
        if l != []:
            print(l[len(l)-1])
            l = l[:len(l)-1]
        else:
            print(-1)    
    elif "size" in x:
        size(l)
    elif "empty" in x:
        empty(l)
    elif "top" in x:
        top(l)

    
        

