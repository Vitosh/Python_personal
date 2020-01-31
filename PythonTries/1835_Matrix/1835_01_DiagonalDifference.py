dims = int(input())
sum_left = 0
sum_right = 0

for left in range(dims):
    new_line = list(map(int, input().split(" ")))
    sum_left += new_line[left]
    sum_right += new_line[dims-1-left]

print(abs(sum_left-sum_right))