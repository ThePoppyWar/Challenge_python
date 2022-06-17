def return_even_number():
    for number in range(2, 20, 2):
        yield number


object_generator = return_even_number()
# print(next(object_generator))
# print(next(object_generator))

# for i in range(10):
#     print(next(object_generator))

# tree = ("*" * n for n in range(5))
# for i in range(5):
#     print(next(tree))

generator_5 = (n * 5 for n in range(1, 11))

for i in range(11):
    print(next(generator_5))
