def fizzbuzz(n):
    for i in range(1, n + 1):
        result = ""
        if i % 3 == 0:
            result += "Fizz"
        if i % 5 == 0:
            result += "Buzz"
        if i % 3 != 0 and i % 5 != 0:
            result = str(i)
        print(result)

print(fizzbuzz(30))

# def fizzbuzz(n):
#     for i in range(1, n+1):
#         if i % 15 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(str(i))
#
# print(fizzbuzz(30))
