dims = int(input())
my_sum = 0

for pos in range(dims):
    new_line = list(map(int, input().split(" ")))
    my_sum += new_line[pos]

print(my_sum)