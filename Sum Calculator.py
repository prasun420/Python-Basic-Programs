"""
WAP to add a stream of numbers given as input by user. Continue to add until the user press q to see
final result.
"""
result = 0
while True:
    n = input("Enter a number to add or 'q' to quit: ")
    if n == 'q':
        print(f"The final result is {result}")
        break
    else:
        result = result + int(n)
        print(f"You sum so far is {result}")
