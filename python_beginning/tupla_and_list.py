lista_1 = [1, 2, 3, True, (1, 2)]
tupla_1 = (4, 5, 6, False, ["x", "y"])

lista_1[2] = "trzy"
print(lista_1)
print("_________________________________")
#
cabinet = [[[], [], []], [[], [], []], [[], [], []]]
cabinet[1][1] = "pen"

for i in cabinet:
    print(i)
#
print("_________________________________")

L = [[34, False], [0], [('abc', 123), {'a': 1, 'x': (True, 'schowany', 5)}]]
print(L[2][1]['x'][1])
print("_________________________________")

K = (('król', {2: 'królewna', 1: ['córka', 'wróbel']}, '5'), ('żółw', 'wiewiórka'))
print(K[0][1][1][1])
#
print("_________________________________")

jezyki = ['python', 'java', 'c#', 'ruby']
jezyki_odwrocone = jezyki[::-1]
jezyki_odwrocone_2 = list(reversed(jezyki))
print(jezyki_odwrocone)
print(jezyki_odwrocone_2)

jezyki_2 = []
for jezyk in jezyki:
    jezyki_2.insert(0, jezyk)
print(jezyki_2)
print("_________________________________")

print("++++++++++++++++++++++++++++++++++")

lista_lista = [11, 22, 33, 56, 4, 55, 23, 45, 5, 12, 25]
s= "a vdvafvafv arvadf45v a5dv5a4fv"
lista_s = list(s)

print(lista_lista[0:5]) #or lista_lista[:5]
print(lista_s[-1:0:2])