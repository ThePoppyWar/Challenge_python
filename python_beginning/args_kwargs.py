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