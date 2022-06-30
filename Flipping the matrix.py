sums = 0
matrix= [[112, 42, 83, 119],

        [56, 125, 56, 49],

        [15, 78, 101, 43],

        [62, 98, 114, 108]]
# for i in range(0, len(matrix)//2):
start = 0
end = len(matrix) - 1

while start<end:
    matrix[start][len(matrix)//2], matrix[end][len(matrix)//2] = matrix[end][len(matrix)//2], matrix[start][len(matrix)//2]
    start+=1
    end-=1
print(matrix)
matrix[0].reverse()
print(matrix)
for i in range(len(matrix)//2):
    for j in range(len(matrix[0])//2):
        sums += matrix[i][j]
print(sums)