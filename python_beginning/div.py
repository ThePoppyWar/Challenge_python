def div(a: int, b: int):
    result = []
    for i in range(a, b+1):
        if i % 2 == 0 and i % 3 != 0:
            result.append(i)
    return result

result = div(0, 20)
print(result)

