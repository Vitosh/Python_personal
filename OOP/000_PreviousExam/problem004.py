import itertools
import math

my_input = '**RLR**'   #input()

my_list = list(my_input)
results = []

count_stars = my_input.count('*')
total = int(math.pow(3, count_stars))

my_lists = [my_list for i in range(total)]
print(total)
helping_list = list(itertools.product('LRS', repeat = total))
i = 0

for list in my_lists:
    current_list = helping_list[i]
    for char in list:
        if char == '*':
            char = current_list[i].pop(0)
    i += 1
    print(list)