import sys

N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(N)]

A.sort()
A.reverse()
print(*A, sep = '\n')