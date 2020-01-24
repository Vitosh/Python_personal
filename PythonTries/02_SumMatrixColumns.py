first_line = input().split(",")
rows = int(first_line[0])
columns = int(first_line[1])

#matrix = [[None for c in range(columns)] for r in range(rows)]
matrix = []
columns_sum = [0 for c in range(columns)]

for r in range(rows):
    new_line = list(map(int, input().split(" ")))
    for c in range(columns):
        columns_sum[c]+= new_line[c]

for c in range(columns):
    print(columns_sum[c])