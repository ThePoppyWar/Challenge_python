x = "costamjestaletegomozeniebyc"

slownik = {}

for litera in x:
    if litera not in slownik.keys():
        slownik[litera] = 1
    else:
        slownik[litera] += 1
print(slownik)


print("________________________________")

S = {x:x+1 for x in range(10000) if x%23 == 0}



liczba = 7430
if liczba not in S.keys():
    print(False)

else:
    print(True)

#or

print(True if 7430 in S.keys() else False)

print("+++++++++++++++++++++++++++++++++++++++++++")

litery = {'m': 1, 'y': 3, 's': 1, 'z': 3, 'd': 2, 'o': 2, \
          'k': 2, 'a': 2, 'u': 2, 'j': 2, 'ą': 2, 'g': 1, \
          't': 1, 'n': 1, 'i': 1, 'e': 1, 'c': 1}

print(True if 3 in litery.values() else False)

print("+++++++++++++++++++++++++++++++++++++++++++")

pensje = {'ksiegowa': 5000, 'kierowca': 4500, 'recepcjonistka': 4000}


result = 0

for i in pensje.values():
    result += i
print(result)

# or
print(sum(pensje.values()))
print("+++++++++++++++++++++++++++++++++++++++++++")