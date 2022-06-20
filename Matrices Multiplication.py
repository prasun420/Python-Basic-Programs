# """
# Matrices multiplication in Python: Matrix A can be multiplied to B if no. of columns of A is equal to
# no. of rows of B
# """
#
# n = int(input("Enter the no. of rows for A: "))
# m = int(input("Enter the no. of cols for A: "))
# n1 = int(input("Enter the no. of rows for B: "))
# m1 = int(input("Enter the no. of cols for B: "))
#
#
# def matrixA(m, n):
#     a = []
#     for i in range(n):
#         rows = []
#         for j in range(m):
#             choice = int(input(f"Enter the [{i}][{j}] element: "))
#             rows.append(choice)
#         a.append(rows)
#     return a
#
#
# A = matrixA(n, m)
# B = matrixA(n1, m1)
#
#
# def result_matrix(n, n1):
#     results = []
#     for i in range(n):
#         rows = []
#         for j in range(n1):
#             # zero = 0
#             rows.append(0)
#         results.append(rows)
#     return results
#
#
# result = result_matrix(n, m1)
#
# print((result))
# for i in range(0, len(result)):
#     for j in range(0, len(result[0])):
#         for k in range(0, len(B)):
#             result[i][j] += (A[i][k] * B[k][j])
# for r in result:
#     print(result)
# import re
# numbers = [ 4, 3, 3, 4, 4, 7, 7]
# k=2
# def check(numbers, k):
#     result = 0
#     for i in range(len(numbers)):
#         if numbers.count(numbers[i]) == k:
#             result = -1
#         else:
#             result = numbers[i]
#     return result
# check(numbers, k)

lst = "this is the man who did this task which is the task to be done by another man"
lst = lst.split(" ")
# print(len(lst))
# print((lst))
def frequency_word(statement):
    lst = statement
    # Your code here
    dict = {}
    # dict1 = {}
    for i in range(len(lst)):
        if lst.count(lst[i])<=1:
            dict1 = {lst[i]:""}
            dict.update(dict1)
        else:
            dict1 ={lst[i]: lst.count(lst[i])}
            dict.update(dict1)
    for key,values in dict.items():
        print(key, values)
frequency_word(lst)
# print(dict)
# print(lst)

# lst = [7,6,7,3,28,7]
# def sorted_elements(arr):
#     # new = []
#     # Your code here
#     # return the list which contains
#     # elements in sorted order
#     arr = list(set(arr))
#     arr.sort()
#     # arr.reverse()
#     return arr
# print(sorted_elements(lst))
