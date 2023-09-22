import sys
N = int(sys.stdin.readline())
print(*sorted(set(list(map(int, sys.stdin.readline().split())))))