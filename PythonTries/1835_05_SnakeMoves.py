def main():
    first_line = input().split(" ")
    rows = int(first_line[0])
    columns = int(first_line[1])

    snake = list(input())
    snake_size = len(snake)
    matrix = [[None for c in range(columns)] for r in range(rows)]
    current_position = 0
    is_reversed = True

    for r in range(rows):
        is_reversed = not is_reversed
        for c in range(columns):
            matrix[r][c] = snake[current_position % snake_size]
            current_position += 1
        if is_reversed:
            matrix[r].reverse()

    print(format_matrix(matrix))
    

def format_matrix(my_matrix):
    return '\n'.join(''.join(str(column) for column in row) for row in my_matrix)

if __name__ == "__main__":
    main()