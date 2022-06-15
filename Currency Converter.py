"""
Create a currency converter
"""
amt = int(input("Enter the amount: "))
lst = []
lst1 = []
result = 0
f = open("currency.txt", "r")
for i in range(1, 53, 1):
    a = f.readline()
    lst.append(a)


for i in range(len(lst)):
    c = lst[i].split('\t')
    lst1.append(c)

for i in range(len(lst1)):
    print(f"{lst1[i][0]}")
cvt = input("Enter in which currency you want to convert from above list: ")

for i in range(len(lst1)):
    if lst1[i][0] == cvt:
        result = amt * float(lst1[i][1])
        print(result)
        break
    else:
        continue
