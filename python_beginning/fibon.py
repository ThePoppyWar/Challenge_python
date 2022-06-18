
def fibonca_r(n):
    if n <= 1:
        return n
    return fibonca_r(n - 1) + fibonca_r(n - 2)

print(fibonca_r(10))


def fiboca_l(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fiboca_l(8))