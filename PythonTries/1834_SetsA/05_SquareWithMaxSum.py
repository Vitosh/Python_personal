first_line = input().split(",")
rows = int(first_line[0])
columns = int(first_line[1])

matrix = []
for r in range(rows):
    new_line = list(map(int, input().split(",")))
    matrix.append(new_line)

matrix2 = matrix
current_max = float('-inf')


for row in range(1, rows):
    for column in range(1, columns):

        current_list = []
        current_list.append(matrix[row-1][column-1])
        current_list.append(matrix[row-1][column])
        current_list.append(matrix[row][column-1])
        current_list.append(matrix[row][column])
        current_row_col_max = sum(current_list)

        if current_row_col_max > current_max:
            current_max = current_row_col_max
            max_square = current_list
            
print("%s %s\n%s %s" %(max_square[0],max_square[1],max_square[2],max_square[3]))
print(current_max)