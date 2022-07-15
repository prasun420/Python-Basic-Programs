"""
Input: No. of rows for the stars say 4
Output: *
        * * *
        * * * * *
        * * * * * * *

Explanation: rows will have odd number of starts
"""
# k variable will store the odd numbers
k = 1
n = int(input("Enter no. of rows: "))
for i in range(1, n+1, 1):
    for j in range(1, k+1, 1):
        print("*", end=" ")
    k += 2
    print("\n")
