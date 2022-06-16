L = [("Anna", 32), ("krzyś", 4), ("Monika", 14), ("Krystyna", 56)]

L_sorted = sorted(L, key=lambda x: x[1])
print(L_sorted)

S = ['Anna', 'Robert', 'Artur', 'Feliks']

S_posortowana = sorted(S, key=lambda x: x[-1])

print(S_posortowana)
