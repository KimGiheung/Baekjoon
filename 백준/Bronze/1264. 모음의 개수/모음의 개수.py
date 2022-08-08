b = ['a','e','i','o','u','A','E','I','O','U']
s = []
while(True):
    s.append(input().lower())
    if s[-1] == "#":
        s.remove(s[-1])
        break
    
for i in s:
    count = 0
    for j in i:
        if j in b: count += 1
    print(count)