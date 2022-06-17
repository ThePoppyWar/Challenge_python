import random


A = [random.randint(0, 100) for i in range(5)]
B = [random.randint(0, 100) for i in range(5)]
H = [random.randint(0, 100) for i in range(5)]

# max_v = 0
# licznik = 0
# for a in A:
#     for b in B:
#         for h in H:
#             licznik += 1
#             if a * b * h > max_v:
#                 max_v = a * b * h
# print(max_v)
# print(licznik)

print(max(A) * max(B) * max(H))

