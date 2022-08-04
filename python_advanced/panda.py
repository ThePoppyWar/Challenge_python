import pandas as pd

# print(dir(pd))


class Container:
    """This is a Container class."""


print(Container.__dict__.keys())

container = Container()

print(type(Container.__dict__))
print(type(container.__dict__))