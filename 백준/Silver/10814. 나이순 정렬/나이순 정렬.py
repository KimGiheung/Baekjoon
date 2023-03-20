import sys
N = int(sys.stdin.readline())

A = [[] for _ in range(N)]
for i in range(N):
    A[i] = input().split()
    A[i][0] = int(A[i][0])
A.sort(key=lambda x : x[0])

for i in range(N):
    print(A[i][0], A[i][1])