import sys
N = int(sys.stdin.readline())

A = [[] for _ in range(N)]
for i in range(N):
    A[i] = sys.stdin.readline().split()
    A[i][1:] = map(int, A[i][1:])

A.sort( key=lambda x : (-x[1], x[2], -x[3], x[0]))




for i in range(N):
    print(A[i][0])
