def soln(mat):
    if not mat or not mat[0]:
        return []
    
    mat_rows = len(mat)
    mat_cols = len(mat[0])
    
    top, right, bottom, left = 0, mat_cols - 1, mat_rows - 1, 0
    ret_mat = []
    
    while top <= bottom and left <= right:
        # Left to right on the top row
        for i in range(left, right + 1):
            ret_mat.append(mat[top][i])
        top += 1
        
        # Top to bottom in the right column
        for i in range(top, bottom + 1):
            ret_mat.append(mat[i][right])
        right -= 1
        
        # Right to left in the bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                ret_mat.append(mat[bottom][i])
            bottom -= 1
            
        # Bottom to top in the left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                ret_mat.append(mat[i][left])
            left += 1

    return ret_mat
matrix = [[1, 2, 3, 4, 5, 6],
          [7, 8, 9, 10, 11, 12],                
          [13, 14, 15, 16, 17, 18],
          [19, 20, 21, 22, 23, 24],
          [25, 26, 27, 28, 29, 30]]

print(soln(matrix))