input()
int_list = [i for i in map(int,input().split())]
int_list.sort()
print(int_list[0], int_list[-1])