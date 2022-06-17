def add_stars(function):
    def function_decorator():
        print("***")
        function()
        print("***")
    return function_decorator()

@add_stars
def f():
    print("Hi I'm funcion f() ")


