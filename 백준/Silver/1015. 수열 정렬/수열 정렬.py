import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = sorted(range(N), key=lambda x: (A[x],x))
C = {}
for new_idx, A_idx in enumerate(B):
    if A[A_idx] not in C:
        C[A[A_idx]] = []
    C[A[A_idx]].append(new_idx)

result = [C[num].pop(0) for num in A]

print(*result, sep = ' ')
