
P = [-10, -7, -5, -3, 0, 3, 5, 21, 68, 341, 500]

our_number = -22
left = 0
right = len(P) - 1

while left <= right:
    middle = (left + right) // 2
    if P[middle] == our_number:
        print(f"Number {our_number} is on the list")
        break
    elif P[middle] < our_number:
        left = middle + 1
    else:
        right = middle - 1
else:
    print(f"Number {our_number} is not on the list")


