import sys
A = sys.stdin.readline().rstrip()
B = [A[-n-1:] for n in range(-1, -len(A)-1 ,-1)]
B.sort(key=lambda x : x)
print(*B, sep = '\n')