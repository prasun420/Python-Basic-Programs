"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example
i. 12.:01:00 PM
Return '12:01:00'.

ii. 12.:01:00 AM
Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing
the input time in 24hour format.

timeConversion has the following parameter(s): string s: a time in 12-hour format
Returns: string: the time in 24-hour format

Input Format:
A single string
that represents a time in 12-hour clock format (i.e.: or hh:mm:ss AM/PM).

Constraints: All input times are valid

Sample Input: 07:05:45PM

Sample Output: 19:05:45

"""
import re
time = input("Enter time: ")
lst = time.split(':')
pat1 = re.compile(r'[0-9]+(PM)')
pat2 = re.compile(r'[0-9]+(AM)')
if bool(re.search(pat1, lst[2])) is True and lst[0] != '12':
    lst[0] = str(int(lst[0]) + 12)
    s1 = ":".join(lst)
    print(s1[:len(s1)-2])
elif bool(re.search(pat2, lst[2])) is True and lst[0] == '12':
    lst[0] = "00"
    s1 = ":".join(lst)
    print(s1[:len(s1) - 2])
else:
    s1 = ":".join(lst)
    print(s1[:len(s1) - 2])