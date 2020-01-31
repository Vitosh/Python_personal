first_line = input().split(" ")
rows = int(first_line[0])
columns = int(first_line[1])
result = 0
matrix = []
for r in range(rows):
    new_line = list(input().split(" "))
    matrix.append(new_line)

for row in range(1, rows):
    for column in range(1, columns):
        if (matrix[row-1][column-1] == matrix[row][column]) \
        and (matrix[row][column-1] == matrix[row][column]) \
        and (matrix[row-1][column] == matrix[row][column]):
            result += 1
print(result)