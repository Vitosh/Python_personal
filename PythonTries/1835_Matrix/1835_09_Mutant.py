is_dead = False
has_escaped = False
rows_total = -1
columns_total = -1
matrix = []

def main():
    
    global rows_total
    global columns_total
    global matrix

    rc = input().split()
    rows_total = int(rc[0])
    columns_total = int(rc[1])
    matrix = []
    
    for _ in range(rows_total):
        line_input = input()
        matrix.append(list(line_input))

    commands_given = list(input())
    i = -1

    player_position = detect_position("P")
    current_row = player_position[0]
    current_column = player_position[1]

    result = ""

    while True:
        i += 1

        command  =  commands_given[i]

        player_position = moving_player(current_row, current_column, command)
        matrix = spread_bunnies()

        current_row = player_position[0]
        current_column = player_position[1]

        if is_dead:
            result = "dead: {} {}".format(current_row, current_column)
            break

        if has_escaped:
            result = "won: {} {}".format(current_row, current_column)
            break

       
    print(format_matrix(matrix))
    print(result)

def moving_player(current_row, current_column, command):

    global has_escaped
    global is_dead
    global matrix
    
    matrix[current_row][current_column] = "."

    if command == "U":
        if current_row == 0:
            has_escaped = True
            return [current_row, current_column]
        elif matrix[current_row - 1][current_column] == "B":
            is_dead = True
        else:
            matrix[current_row - 1][current_column]= "P"
        return [current_row - 1, current_column]

    elif command == "R":
        if current_column == columns_total-1:
            has_escaped = True
            return [current_row, current_column]
        elif matrix[current_row][current_column + 1] == "B":
            is_dead = True
        else:
            matrix[current_row][current_column + 1] = "P"
        return [current_row, current_column + 1]
    
    elif command == "D":
        if current_row == rows_total - 1:
            has_escaped = True
            return [current_row, current_column]
        elif matrix[current_row + 1][current_column] == "B":
            is_dead = True
        else:
            matrix[current_row + 1][current_column] = "P"
        return [current_row + 1, current_column]

    elif command == "L":
        if current_column == 0:
            has_escaped = True
            matrix[current_row][current_column] = "."
            return [current_row, current_column]
        elif matrix[current_row][current_column - 1] == "B":
            is_dead = True
        else:
            matrix[current_row][current_column - 1] = "P"
        return [current_row, current_column - 1]

def detect_position(my_char):

    global matrix
    
    for row in range(rows_total):
        for column in range(columns_total):
            if matrix[row][column] == my_char:
                return [row,column]

def spread_bunnies():

    global matrix
    global rows_total
    global columns_total
    global is_dead

    for row in range(rows_total):
        for column in range(columns_total):
            if matrix[row][column] == "B":

                if row < (rows_total - 1):
                    if matrix[row + 1][column] == "P":
                        is_dead = True
                    if matrix[row + 1][column] != "B":
                        matrix[row + 1][column] = "*"

                if row > 0:
                    if matrix[row - 1][column] == "P":
                        is_dead = True
                    if matrix[row - 1][column] != "B":
                        matrix[row - 1][column] = "*"

                if column > 0:
                    if matrix[row][column-1] == "P":
                        is_dead = True
                    if matrix[row][column - 1] != "B":
                        matrix[row][column - 1] = "*"

                if column < (columns_total - 1):
                    if matrix[row][column+1] == "P":
                        is_dead = True
                    if matrix[row][column + 1] != "B":
                        matrix[row][column + 1] = "*"
                
    for row in range(rows_total):
            for column in range(columns_total):
                if matrix[row][column] == "*":
                    matrix[row][column] = "B"

    return matrix

def format_matrix(my_matrix):
    return '\n'.join(''.join(str(column) for column in row) for row in my_matrix)

if __name__ == "__main__":
    main()
