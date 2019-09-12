print("hello")
a = 10
b = 35
c = a+b
print(c)


def fact(n):
    return fact_iter(n, 1)


def fact_iter(number, product):
    if number == 1:
        return product
    print(number-1, "-->", number*product)
    return fact_iter(number-1, number*product)


print(fact(7))
