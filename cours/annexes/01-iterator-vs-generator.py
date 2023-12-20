def range_2(n):
    compteur = 0
    while compteur < n:
        yield compteur
        compteur += 1


def walk():
    # blabla
    return range_2(6)


range = walk()
print(range, type(range))
for element in range:
    print(element)


def scandir():
    # blabla
    return [1, 2, 3, 4, 5]

res = scandir()
print(res, type(res))
for element in res:
    print(element)
