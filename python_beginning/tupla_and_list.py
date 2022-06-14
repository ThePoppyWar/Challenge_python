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
