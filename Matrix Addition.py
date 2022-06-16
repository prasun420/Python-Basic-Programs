"""
Add a m*n matrix to another m*n matrix:
"""

row = int(input("Enter the no. of rows: "))
column = int(input("Enter the no. of columns: "))


def matrix(row, column):
    o = []
    for rows in range(row):
        rowsM = []
        for columns in range(column):
            inputs = int(input(f"Enter the [{rows}][{columns}] element: "))
            rowsM.append(inputs)
        o.append(rowsM)
    return o


print("Enter matrix A")
A = matrix(row, column)
print(A)
print("Enter matrix B")
B = matrix(row, column)
print(B)


def add(A, B):
    outer = []
    for i in range(len(B)):
        rowss = []
        for j in range(len(B[0])):
            rowss.append(A[i][j] + B[i][j])
        outer.append(rowss)
    return outer


print(f"The sum of the 2 matrices is {add(A, B)}")
