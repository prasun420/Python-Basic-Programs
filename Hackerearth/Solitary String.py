tc = int(input("Enter number of test cases: "))
# Solution One
print("----------------Method I---------------")
for k in range(tc):
    s = input("Enter the String:")
    """Optimized solution. This solution will pass for all large Test Cases with TLE and Memory exceeded"""
    res = -1
    for i in s:
        lindex = s.index(i)
        rind = s.rindex(i)
        res = max(res, rind - lindex - 1)
    print(res)

# Solution 2: Without using in-built functions:

"""This solution may show TLE and memory exceeded error in large test cases:"""
diff = 0
lst = []
temp = 0
print("----------------Method II---------------")
for k in range(tc):
    s = input("Enter the String:")

    if len(s) == 1:
        lst.append(-1)
    else:
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    diff = j - i - 1
                    if diff > temp:
                        temp = diff
                        lst.append(temp)
                else:
                    lst.append(-1)

    print(max(lst))
