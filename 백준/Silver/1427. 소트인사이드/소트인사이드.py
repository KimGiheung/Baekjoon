import sys

A = list(sys.stdin.readline())

A.sort()
A.reverse()

print(*A, sep = '')