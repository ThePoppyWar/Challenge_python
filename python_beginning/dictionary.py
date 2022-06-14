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
