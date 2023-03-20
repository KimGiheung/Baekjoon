import sys
N = int(sys.stdin.readline())

A = [input() for _ in range(N)]
A = list(set(A))
A.sort( key=lambda x : (len(x), x))


print(*A, sep='\n')
