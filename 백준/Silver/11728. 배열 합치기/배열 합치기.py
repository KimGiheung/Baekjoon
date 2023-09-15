import sys
a, b = map(int,sys.stdin.readline().split())
A = [0 for i in range(a)]
B = [0 for i in range(b)]

str = list(map(int, sys.stdin.readline().split()))

if a == len(str):
    for i in range(a):
        A[i] = str[i]

str = list(map(int, sys.stdin.readline().split()))
if b == len(str):
    for i in range(b):
        B[i] = str[i]
 
print(*sorted(A+B))