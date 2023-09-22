import sys
A = [int(sys.stdin.readline()) for _ in range(8)]
B = list(enumerate(A, start=1))
B.sort(key=lambda y:y[1])
C = B[-1:-6:-1]
print(sum(b for a, b in C))
print(*sorted([a for a, b in C]), sep = " ")