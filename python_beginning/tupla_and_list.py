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

K = (('król', {2:'królewna', 1: ['córka', 'wróbel']},'5'),('żółw', 'wiewiórka'))
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