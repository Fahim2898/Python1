num = [1, 2, 3, 4, 5]


def check(x):
    return x % 2 == 1


result = list(filter(check, num))

print(result)