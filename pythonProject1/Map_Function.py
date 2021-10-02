def squre(x):
    return x*x


num = [1, 2, 3, 4, 5]

# map function work on 1 function & 1 list
result = list(map(squre, num))
print(result)