"""
Given an array of integers, where all elements but one occur twice, find the unique element.

Example: a =[1, 2, 1, 2, 3, 3, 4]
The unique element is 4

Function Description:

Complete the lonelyinteger function in the editor below.

lonelyinteger has the following parameter(s):
int a[n]: an array of integers

Returns: int: the element that occurs only once

Input Format

The first line contains a single integer n,the number of integers in the array.
The second line contains n space-separated integers that describe the values in a

Constraints
i. 1<=n<=100
ii. It is guaranteed that n is an odd number and that there is one unique element.
iii. 0<=a[i]<=100 where 0<=i<n
"""
lst = []
n = int(input("Enter the size of array in odd number: "))
for j in range(n):
    lst.append(int(input(f"Enter the {j} index element of array: ")))


def unique(lst1):
    result = 0
    for i in lst:
        c = lst.count(i)
        if c == 1:
            result = i
    return result


print(f"The unique element in {lst} is {unique(lst)}")
