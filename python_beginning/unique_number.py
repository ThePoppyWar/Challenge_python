# the first way
def unique_number(list_1):
    list_2= []
    for i in list_1:
        if i not in list_2:
            list_2.append(i)
    return list_2


list_number = [1, 2, 3, 3, 2, 1, 2, 3]
print(unique_number(list_number))

# the second way
list_set = list(set(list_number))
print(list_set)

#how many unique element has list

A = [1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 7, 5, 43, 4, 6]

list_2 = list(set(A))
print(len(list_2))

# or

def count_unique_elements(list_A):
    list_B = []
    for i in list_A:
        if i not in list_B:
            list_B.append(i)
    return len(list_B)

list_number_1 = [1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 7, 8, 10, 9]
print(count_unique_elements(list_number_1))