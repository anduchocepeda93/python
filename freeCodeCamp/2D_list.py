number_grid = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]
print(number_grid)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(number_grid[0][0])  # Output: 1
print(number_grid[1][2])  # Output: 6
print(number_grid[2][1])  # Output: 8
print(number_grid[0][2])  # Output: 3

for row in number_grid:
    print(row)  # Output: [1, 2, 3], [4, 5, 6], [7, 8, 9]

for row in number_grid:
    for col in row:
        print(col)  # Output: 1, 2, 3, 4, 5, 6, 7, 8, 9
        
