def main():
    
    size = int(input())
    matrix = []

    for _ in range(size):
        line_input = input()
        matrix.append(list(map(int,line_input.split())))

    line_input = input()
    line_input = line_input.replace(' ',',')
    bomb_lines = list(map(int,line_input.split(',')))

    for i in range(len(bomb_lines)):
        if i % 2 == 0:
            bomb_row = bomb_lines[i]
            bomb_col = bomb_lines[i+1]

            matrix = trigger_bomb(bomb_row, bomb_col, matrix)

    sum_of_alive = 0
    count_of_alive = 0

    for row in range(size):
        for col in range(size):
            if matrix[row][col] > 0:
                sum_of_alive += matrix[row][col]
                count_of_alive += 1

    print("Alive cells: %s"%count_of_alive)
    print("Sum: %s"%sum_of_alive)
    print(format_matrix(matrix))

def trigger_bomb(bomb_row, bomb_col, matrix):

    bomb_power = matrix[bomb_row][bomb_col]
    if bomb_power < 1:
        return matrix
    
    size = len(matrix)
    matrix[bomb_row][bomb_col] = 0

    #up
    if bomb_row > 0:
        if matrix[bomb_row-1][bomb_col] > 0:
            matrix[bomb_row-1][bomb_col] -= bomb_power
    
    #down
    if bomb_row < size-1:
        if matrix[bomb_row+1][bomb_col] > 0:
            matrix[bomb_row+1][bomb_col] -= bomb_power

    #left
    if bomb_col > 0:
        if matrix[bomb_row][bomb_col-1] > 0:
            matrix[bomb_row][bomb_col-1] -= bomb_power

    #right
    if bomb_col < size-1:
        if matrix[bomb_row][bomb_col+1] > 0:
            matrix[bomb_row][bomb_col+1] -= bomb_power

    #left up diagonal 
    if bomb_row > 0 and bomb_col > 0:
        if matrix[bomb_row-1][bomb_col-1] > 0:
            matrix[bomb_row-1][bomb_col-1] -= bomb_power

    #right up diagonal 
    if bomb_row > 0 and bomb_col < size-1:
        if matrix[bomb_row-1][bomb_col+1] > 0:
            matrix[bomb_row-1][bomb_col+1] -= bomb_power

    #right down diagonal 
    if bomb_row < size-1 and bomb_col < size-1:
        if matrix[bomb_row+1][bomb_col+1] > 0:
            matrix[bomb_row+1][bomb_col+1] -= bomb_power

    #left down diagonal 
    if bomb_row < size-1 and bomb_col > 0:
        if matrix[bomb_row+1][bomb_col-1] > 0:
            matrix[bomb_row+1][bomb_col-1] -= bomb_power
    return matrix


def format_matrix(my_matrix):
    return '\n'.join(' '.join(str(column) for column in row) for row in my_matrix)

if __name__ == "__main__":
    main()