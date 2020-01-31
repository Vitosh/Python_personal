dims = int(input())

#matrix = [[None for c in range(dims)] for r in range(dims)]
matrix = []

for pos in range(dims):
    my_input = input()
    matrix.append(list(my_input))

symbol = input()
result = ""

for row in range(dims):
    for col in range(dims):
        if (symbol == matrix[row][col]) and (result == ""):
            result = "(%s, %s)" %(row, col)

if result == "":
    result = "%s does not occur in the matrix" % symbol

print(result)