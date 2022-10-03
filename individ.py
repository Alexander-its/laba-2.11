def f(a, b):
    return a + b

def foo(a, b, func):
    def inner(a, b):
        return f"ДЛя значений a, b функция {func(a,b) = }"
    return inner(a, b)

print(foo(2, 7, f))
