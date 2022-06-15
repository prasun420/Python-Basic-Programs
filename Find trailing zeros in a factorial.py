"""
1. Find the factorial of a number
2. Find the trailing zeroes in the factorial found above
"""


choice = int(input("Enter a number: "))
fact = 1
for i in range(1, choice+1, 1):
    fact = fact*i
print(f"The factorial of {choice} is {fact}")


n = str(fact)
count = len(n) - len(n.rstrip('0'))
lst = n.split("0")
print(f"The no of trailing zeros in {fact} is {count}")
