def main():
    
    size = int(input())
    matrix = []
    commands_given = list(input().split())

    for _ in range(size):
        line_input = input()
        matrix.append(list(line_input.split()))

    coal_total = 0
    for row in range(size):
        for col in range(size):
            if get_info_of_field(row,col,matrix)=='c':
                coal_total+=1

    commands = commands_given[::-1]
    current_position = locate_start(matrix)
    game_over = False
    all_coals = False

    while len(commands) > 0:

        current_command = commands.pop()
        current_position = move(current_position[0],current_position[1],matrix,current_command)
        
        row = current_position[0]
        col = current_position[1]

        
        if get_info_of_field(row,col,matrix) == 'e':
            print("Game over! ({}, {})".format(row,col))
            game_over = True
            break
        elif get_info_of_field(row,col,matrix) == 'c':
            coal_total -= 1
        
        if coal_total == 0:
            print("You collected all coals! ({}, {})".format(row,col))
            all_coals = True
            break
        
        matrix[current_position[0]][current_position[1]] = 'o'
    
    if all_coals:
        pass
    elif game_over:
        pass
    else:
        print("{} coals left. ({}, {})".format(coal_total, current_position[0],current_position[1]))

def locate_start(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == 's':
                return [row,col]

def get_info_of_field(row, col, matrix):
    return matrix[row][col]

def move(row, col, matrix, order): 
    movement = []

    if order == "left":
        if col < 1:
            movement = (row,col)
        else:
            movement = (row, col-1)
    elif order == "up":
        if row < 1:
            movement = (row, col)
        else:
            movement = (row - 1, col)
    elif order == "right":
        if col >= len(matrix)-1:
            movement = (row, col)
        else:
            movement = (row, col+1)
    elif order == "down":
        if row >= len(matrix) - 1:
            movement = (row, col)
        else:
            movement = (row+1, col)
    return movement


def format_matrix(my_matrix):
    return '\n'.join(' '.join(str(column) for column in row) for row in my_matrix)

if __name__ == "__main__":
    main()