import sys

N = int(sys.stdin.readline())

A = []
memo = []

# 삼각형, 메모할 삼각형
for i in range(N):
    memo.append([0]*N)
    A.append(list(map(int, sys.stdin.readline().split())))

# print(*A, sep = '\n')

memo[0][0] = A[0][0]
for i in range(1, N):
    for j in range(len(A[i])):
        if j-1 >= 0:
            if j != len(A[i])-1:
                memo[i][j] = max(memo[i-1][j], memo[i-1][j-1]) + A[i][j]
            else:
                memo[i][j] = memo[i-1][j-1] + A[i][j]
        else:
            memo[i][j] = memo[i-1][j] + A[i][j]



# print(*memo, sep = '\n')
print(max(memo[N-1]))