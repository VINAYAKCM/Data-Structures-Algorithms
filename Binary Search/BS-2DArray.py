def search(matrix, target):
    r = 0
    c = len(matrix[0]) - 1

    while r < len(matrix) and c >= 0:
        #You start at row 1, value 1 of the row as lower bound and len(row) -1 = column position as upper bound
        if matrix[r][c] == target:
            return [r, c]

        if matrix[r][c] < target:
            r += 1 #Eliminate current row and move to next one
        else:
            c -= 1 #Eliminate current column and move -1 column

    return [-1, -1]

matrix = [[10, 20, 30],
          [35, 40, 45],
          [50, 55, 60]]
print("Co-ordinates of the target in matrix: ", search(matrix, 35))