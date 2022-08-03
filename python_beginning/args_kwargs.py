def sample(*args):
    print(len(args))
    print(args)


sample(3, "a", False)


def stick(*args):
    result = ''
    for arg in args:
        result += str(arg)
    return result


print(stick(4, 5))
print(stick("Python", " ", 5, "3.5"))


def sample2(**kwargs):
    print(len(kwargs))
    print(kwargs)


sample2()

sample2(ver1="puthon")
sample2(ver1="puthon", ver2="3.8")

print("-----------------------------------------------------------")


def func(**kwargs):
    for item in kwargs.items():
        print(item)


func(name="jan", nazwisko="kowalski")


def hello(**kwargs):
    if 'name' in kwargs:
        print(f"Hello {kwargs['name']}")
    else:
        print("Hello")


hello()
hello(name="John")
print("-----------------------------------------------------------")


def sum_int(**kwargs):
    if kwargs:
        result = 0
        for kwarg in kwargs.values():
            if isinstance(kwarg, int):
                result += kwarg
        return result
    return None


sum_int()
print(sum_int(name='John'))
print(sum_int(name='John', game1=33, game2=333, retro=0.5))

print("-----------------------------------------------------------")


def sample3(*args, **kwargs):
    print(args)
    print(kwargs)


sample3()

sample3(3, 4, 5, va1='ore', va3='more')

books = {"horror": "Smentarz dla zwierząt", "fantastyka": "Zakon drzewa pomarańczy"}
sample3(**books)
number = (10, 40, 30)
sample3(*number, **books)
print("-----------------------------------------------------------")


def stick(*args):
    args = [arg for arg in args if isinstance(arg, str)]
    result = ','.join(args)
    return result


print(stick('sport', 'summer'))
print(stick(3, 5, 7))
print(stick(False, 'time', True, 'workout', [], 'gym'))
