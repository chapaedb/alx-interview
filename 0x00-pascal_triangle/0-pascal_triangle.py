#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]  # Initialize the triangle with the first row

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # Every row starts with 1
        # Generate the middle values
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # Every row ends with 1
        triangle.append(new_row)
    
    return triangle

# The provided main function to print the triangle
def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

