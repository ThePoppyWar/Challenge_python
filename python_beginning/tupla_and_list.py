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


print(lista_lista[0:5]) #or lista_lista[:5]
print(s[-1::-2])
print("++++++++++++++++++++++++++++++++++")

a = "python.py"
b = "python_not.txt"

def check_python(name):
    if name[0:6] == "python" and name[-3:] == ".py":
        return True
    else:
        return False

print(check_python(a))
print(check_python(b))

print("++++++++++++++++++++++++++++++++++")
imiona = ["Stasia", "Czesiu", "Krysia", "Mysia", "Witold"]

num = 1
for imie in imiona:
    print(num, imie)
    num += 1

# or
print("--------------------------------------------")
for num, imie in enumerate(imiona, 1):
    print(num, imie)

print("--------------------------------------------")

liczby = [4, 5, 7, -3, 2, 8, -10, 15]

# print("pierwszy sposób")
# liczby = sorted(liczby)
# print(liczby[-1] - liczby[0])

# print("drugi sposób")
# najmniejsza= liczby[0]
# najwieksza = liczby[0]
#
# for liczb in liczby:
#     if liczb < najmniejsza:
#         najmniejsza = liczb
#     elif liczb > najwieksza:
#         najwieksza = liczb
# print(najwieksza - najmniejsza)

print("trzeci sposób")
print(max(liczby) - min(liczby))