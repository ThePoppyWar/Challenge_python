counter = 1


def update_counter():
    global counter
    counter += 1
    print(counter)


update_counter()

print("--------------------------------------------------------")


def display_info(number_of_updates=1):
    counter = 0
    dash_counter = ''

    def update_counter():
        nonlocal counter
        counter += 1
        nonlocal dash_counter
        dash_counter += '-'

    [update_counter() for _ in range(number_of_updates)]

    print(counter)
    print(dash_counter)


display_info(50)
