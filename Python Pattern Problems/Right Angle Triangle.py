"""
Input: No. of rows for the stars say 4
Output: *
        * *
        * * *
        * * * *
"""

n = int(input("Enter the number of rows: "))

# First for loop is for the no. of rows
for i in range(n):

    # Second for loop is for the no. of columns
    for j in range(0, i+1, 1):
        print("*", end=" ")

    """Once the second for loop ends 2nd print statement will move 
    the control to next line and start printing from next line"""
    print("\n")
