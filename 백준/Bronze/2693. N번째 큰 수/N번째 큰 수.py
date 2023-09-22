import sys
N = int(sys.stdin.readline())
A = [sorted(list(map(int, sys.stdin.readline().split()))) for _ in range(N)]
print(*[A[a][-3] for a in range(N)],sep = '\n')




