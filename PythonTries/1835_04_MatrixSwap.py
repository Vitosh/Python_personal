def main():
    first_line = input().split()
    rows = int(first_line[0])
    columns = int(first_line[1])

    matrix = []
    for _ in range(rows):
        new_line = list(map(int, input().split()))
        matrix.append(new_line)

    command = input()
    while command.split()[0] != "END":
        new_line = list(command.split())
        if new_line[0] != "swap" or len(new_line) != 5:
            print("Invalid input!")
        else:
            row1 = int(new_line[1])
            col1 = int(new_line[2])
            row2 = int(new_line[3])
            col2 = int(new_line[4])
            if any(i < 0 for i in [row1, col1, row2, col2]):
                print("Invalid input!")
            elif any(i >= rows for i in [row1,row2]):
                print("Invalid input!")
            elif any(i >= columns for i in [col1, col2]):
                print("Invalid input!")
            else:
                matrix[row2][col2], matrix[row1][col1] = matrix[row1][col1], matrix[row2][col2]
                print(format_matrix(matrix))
        command = input()

def format_matrix(my_matrix):
    return '\n'.join(' '.join(str(column) for column in row) for row in my_matrix)

if __name__ == "__main__":
    main()