def first_function():
    sum = 0
    for i in range(100):
        sum += i

    print('Tong cac so tu 0 den 99 la', sum)


first_function()
first_function()
first_function()


def f(x):
    return x ** 2 - 2 * x + 3


y = f(10)
print(y)


def return_none():
    x = 10
    y = 11


print(return_none())
