"""
Given a string without spaces, the task is to remove duplicates from it.

Note: The original order of characters must be kept the same.

Example 1:

Input: S = "zvvo"
Output: "zvo"
Explanation: Only keep the first
occurrence

Example 2:

Input: S = "gfg"
Output: gf
Explanation: Only keep the first
occurrence

Your task:
Your task is to complete the function removeDups() which takes a single string as input and
returns the string. You need not take any input or print anything.


Expected Time Complexity: O(|s|)
Expected Auxiliary Space: O(constant)

Constraints:
1 <= |S| <= 105
S contains lowercase english alphabets
"""

s = "zvvo"
# Method 2
dict1 = {}
for i in range(len(s)):
    dicts = {s[i]: i}
    dict1.update(dicts)
print("".join(dict1))

# Method 2
sets = set()
s1 = ""
for i in s:
    if i not in sets:
        s1 += i
        sets.add(i)
print(s1)
