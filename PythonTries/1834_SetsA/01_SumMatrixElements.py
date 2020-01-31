first_line = input().split(",")
rows = int(first_line[0])
columns = int(first_line[1])

#matrix = [[None for c in range(columns)] for r in range(rows)]
matrix = []
matrix_sum = 0

for r in range(rows):
    new_line = list(map(int, input().split(",")))
    matrix_sum += sum(new_line)
    matrix.append(new_line)

print(matrix_sum)
print(matrix)