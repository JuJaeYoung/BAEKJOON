import sys

n = int(sys.stdin.readline())

num_stack = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x != 0:
        num_stack.append(x)

    else:
        num_stack.pop()

print(sum(num_stack))
