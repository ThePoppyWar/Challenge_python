def safe_get(l, index):
    try:
        return l[index]
    except IndexError as e:
        return None
    except TypeError as exception:
        return None

print(safe_get([1,2,3,4,5], 2))
print(safe_get([1,2,3,4,5], 8))
print(safe_get([1,2,3,4,5], 'a'))
