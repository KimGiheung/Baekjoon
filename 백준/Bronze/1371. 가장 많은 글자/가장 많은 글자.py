import sys
s = sys.stdin.read()

a = [0] * 26
for i in s:
    if i.islower():
        a[ord(i) - 97] += 1
print(*[chr(i+97) for i in range(26) if a[i] == max(a)], sep = '')
