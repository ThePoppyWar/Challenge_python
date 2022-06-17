def add_things(a, b):
    return a + b


def test_add_int():
    assert add_things(2, 5) == 7


def test_add_str():
    assert add_things("1", "C") == "1C"



