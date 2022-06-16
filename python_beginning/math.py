def devidable_by_2(first, second):
    return True if first % second == 0 else False

def devidable_by_2_1(first, second):
    return (first % second == 0)

print(devidable_by_2(4, 6))
print(devidable_by_2(4, 2))
print('+++++++++++++++++++++++')
print(devidable_by_2(10, 5))
print(devidable_by_2(1000, 7))

# funkcja

def add_to_list(n, lista = []):
    lista.append(n)
    print(lista)

add_to_list(1)
add_to_list(2, [4, 5])
add_to_list(3)
