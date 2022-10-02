import sys


N = int(input())
A = [int(sys.stdin.readline()) for _ in range(N)]
A.sort()
print(*A, sep = "\n")