import math

my_input = input()
my_list = my_input.split()
my_queue = []
action = ['+', '-', '*', '/']
result = 0
is_first = True

for m in my_list:
    if m not in action:
        my_queue.append(m)
    else:
        if m == "+":
            while len(my_queue):
                if is_first:
                    is_first = False
                    result = int(my_queue.pop(0))
                else:
                    result = math.floor(result + int(my_queue.pop(0)))
        if m == "-":
            while len(my_queue):
                if is_first:
                    is_first = False
                    result = int(my_queue.pop(0))
                else:
                    result = math.floor(result - math.floor(int(my_queue.pop())))
        if m == "/":
            while len(my_queue):
                if is_first:
                    is_first = False
                    result = int(my_queue.pop(0))
                else:
                    result = math.floor(result /  int(my_queue.pop()))
        if m == "*":
            while len(my_queue):
                if is_first:
                    is_first = False
                    result = int(my_queue.pop(0))
                else:
                    result = math.floor(result*int(my_queue.pop()))

print(result)