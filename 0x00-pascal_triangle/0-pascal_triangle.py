#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []
    
    pascal_triangle = [[1]]
    
    for i in range(1, n):
        prev_row = pascal_triangle[-1]
        curr_row = [1]
        for j in range(1, i):
            curr_row.append(prev_row[j - 1] + prev_row[j])
        curr_row.append(1)
        pascal_triangle.append(curr_row)
    
    return pascal_triangle
