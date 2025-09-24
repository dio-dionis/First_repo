def first(size, *ass ):
    return size + len(ass)


def second(size, **egs):
    return size + len(egs)

print(first(10, 20, 30))
print(second(10, a=20, b=30))

