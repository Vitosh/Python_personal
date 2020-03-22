import itertools
import json

my_product = itertools.product((1, 2, 3, 4), repeat=3)
print (json.dumps(list(my_product), indent = 2, sort_keys = True))

my_permutation = itertools.permutations((1, 2, 3, 4), 3)
print (list(my_permutation))

my_combination = itertools.combinations((1, 2, 3, 4), 3)
print(list(my_combination))

lottery_numbers = list(range(1,50))
print(lottery_numbers)
lottery_combinations = itertools.combinations(lottery_numbers, 6)
print(len(list(lottery_combinations)))