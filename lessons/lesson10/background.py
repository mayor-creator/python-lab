# *args many positional arguments
def add(*args):
    total = 0
    for num in args:
        total += num
    return total


result = add(1, 4, 10, 20)
print(result)
print(add(34, 35, 49, 40))


# kwargs
def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiple"]
    print(n)


calculate(2, add=3, multiple=5)
