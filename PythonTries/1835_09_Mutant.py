def main():
    
    rc = input().split()
    rows_total = int(rc[0])
    columns_total = int(rc[1])
    matrix = []
    
    for _ in range(rows_total):
        line_input = input()
        matrix.append(list(line_input))

    commands_given = list(input())
    i = 0

    player_position = detect_position(matrix, rows_total, columns_total, "P")
    result = ""

    while True:

        command  =  commands_given[i]
        i += 1

        current_row = player_position[0]
        current_column = player_position[1]

        player_is_alive = is_player_alive(matrix, rows_total, columns_total, "P")
        player_has_escaped = has_player_escaped(matrix, rows_total, columns_total)

        if not player_is_alive:
            result = "dead:"
            break            

        player_has_escaped = has_player_escaped(matrix, rows_total, columns_total)

        if player_has_escaped:
            result = "won:"
            break      

        new_position = moving_player(matrix, current_row, current_column, command)
        matrix = fix_matrix(matrix, player_position, new_position)
        player_position = new_position
        matrix = spread_bunnies(matrix,rows_total,columns_total)

    
    print(result)
    print(format_matrix(matrix))

def fix_matrix(matrix, player_position, new_position):

    old_row = player_position[0]
    old_column = player_position[1]

    new_row = new_position[0]
    new_column = new_position[1]

    matrix[old_row][old_column] = "."
    matrix[new_row][new_column] = "P"

    return matrix

def is_player_alive(matrix, rows_total, columns_total, my_char):

    for row in range(rows_total):
        for column in range(columns_total):
            if matrix[row][column] == my_char:
                return True
    return False


def moving_player(matrix, current_row, current_column, command):

    if command == "U":
        return [current_row - 1, current_column]
    elif command == "R":
        return [current_row, current_column + 1]
    elif command == "D":
        return [current_row + 1, current_column]
    elif command == "L":
        return [current_row, current_column - 1]

def detect_position(matrix, rows_total, columns_total, my_char):
    
    for row in range(rows_total):
        for column in range(columns_total):
            if matrix[row][column] == my_char:
                return [row,column]

def spread_bunnies(matrix, rows_total, columns_total):
    
    for row in range(rows_total):
        for column in range(columns_total):
            if matrix[row][column] == "B":

                if row < (rows_total - 1):
                    matrix[row + 1][column] = "*"

                if row > 0:
                    matrix[row - 1][column] = "*"

                if column > 0:
                    matrix[row][column - 1] = "*"

                if column < (columns_total - 1):
                    matrix[row][column + 1] = "*"
                
    for row in range(rows_total):
            for column in range(columns_total):
                if matrix[row][column] == "*":
                    matrix[row][column] = "B"

    return matrix

def has_player_escaped(matrix, rows_total, columns_total):
    
    for row in range(rows_total):
        for column in range(columns_total):
            if matrix[row][column] == "P":
                if row == 0 or row == rows_total or column == 0 or column == columns_total:
                    return True
    return False

def format_matrix(my_matrix):
    return '\n'.join(''.join(str(column) for column in row) for row in my_matrix)

if __name__ == "__main__":
    main()