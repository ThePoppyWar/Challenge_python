def sample():

    num1 = 10

    def inner():
        nonlocal num1
        num1 += 20
        print(num1)

    print(num1)
    inner()
    print(num1)

sample()