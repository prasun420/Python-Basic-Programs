"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
That is left-to-right and right-to-left diagonals
"""
row = int(input("Enter the no. of rows of the matrix: "))
columns = int(input("Enter the no. of columns of the matrix: "))
lst = []
for i in range(row):
    row = []
    for j in range(columns):
        row.append(int(input(f"Enter the [{i}][{j}]th element: ")))
    lst.append(row)

sum1 = 0
sum2 = 0
"""
To find the left to right diagonal find the nth element of nth row.
For eg: 2nd element in 2nd row will be diagonal element 
"""
for i in range(len(lst)):
    for j in range(len(lst[0])):
        # print(lst[i][i])
        sum1 = sum1+lst[i][i]
        break
# print(sum1)

"""
To find the right-to-left diagonal reverse every list of list and find the nth element
of nth row
"""

for i in range(len(lst)):
    lst[i].reverse()
    for j in range(len(lst[0])):
        # print(lst[i][i])
        sum2 = sum2 + lst[i][i]
        break

# print(sum2)

print(f"The absolute sum of the diagonals of a matrix is: {abs(sum1 - sum2)}")
