import sys
N = int(sys.stdin.readline())

A = [[] for _ in range(N)]
for i in range(N):
    A[i] = sys.stdin.readline().split()
    A[i][1:] = map(int, A[i][::-1][:3])

A.sort(key=lambda x : (x[1], x[2], x[3]))



older       = 0
younger     = -1



print(A[younger][0])
print(A[older][0])
        
        