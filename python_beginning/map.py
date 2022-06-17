surname = ['jan kowal', 18, "ANNA KAROLAK", "jÓzek BRYK", ["nie", "wasza", "sprawa"], "Robert wąŻ"]

just_surname = list(filter(lambda x:type(x) is str, surname))
print(just_surname)

right_surname = list(map(lambda x:x.lower().title(), just_surname))
print(right_surname)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9]

B = list(filter(lambda x: x % 2 == 0, A))
C = list(map(lambda x: x * 10, B))

print(C)