import sys
w    = [int(sys.stdin.readline()) for _ in range(10)]
k    = [int(sys.stdin.readline()) for _ in range(10)]
print(sum([w.pop(w.index(max(w))) for _ in range(3)]),sum([k.pop(k.index(max(k))) for _ in range(3)]))

