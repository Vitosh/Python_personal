def get_magic_triangle(n):
    triangle = [[1] * row for row in range(1,n+1)]
    for row in range(2, n):
        for col in range(1, row):
            triangle[row][col] = triangle[row-1][col-1] + triangle[row-1][col]
    return triangle

n = int(input())
result = get_magic_triangle(n)
print(result)