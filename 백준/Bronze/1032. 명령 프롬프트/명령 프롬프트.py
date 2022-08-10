N = int(input())
file_name = []
result = ""
for i in range(N):
    file_name.append(input())


for j in range(len(file_name[0])):
    check = True
    for k in file_name:
        if file_name[0][j] == k[j]:
            continue
        else:
            check = False
    if check == True:
        result += file_name[0][j]
    else:
        result += "?"

print(result)