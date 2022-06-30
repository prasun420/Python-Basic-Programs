"""
Julius Caesar protected his confidential information by encrypting it using a cipher.
Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of
the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y
and z would map to z, a, b and c.
"""

s = input("Enter the string: ")
k = int(input("Enter the number by which the alphabets should shift: "))
lst = []
lst1 = []
for i in s:
    lst.append(i)

for i in lst:
    if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
        if 65 <= ord(i) <= 90:
            i = chr(ord(i) + k)
            while ord(i) > 90:
                i = chr(ord(i) - 26)
        elif 97 <= ord(i) <= 122:
            i = chr(ord(i) + k)
            while ord(i) > 122:
                i = chr(ord(i) - 26)

    lst1.append(i)
print(''.join(lst1))
