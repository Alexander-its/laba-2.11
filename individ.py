#Используя замыкания функций, объявите внутреннюю функцию, которая принимает два
#параметра a , b , а затем, возвращает строку в формате: Для значений a, b функция f(a,b) =
#<число> где число  это вычисленное значение функции f . Ссылка на f передается как
#аргумент внешней функции. Вызовите внутреннюю функцию замыкания и отобразите на
#экране результат ее работы. Функцию f придумайте самостоятельно (она должна что то
#делать с двумя параметрами a , b и возвращать результат).

#!/usr/bin/env python3
# -*- coding: utf -8 -*-

if __name__ == '__main__':
    
    def f(a, b):
        return a + b
    
    def foo(a, b, func):
        def inner(a, b):
            return f"ДЛя значений a, b функция {func(a,b) = }"
        return inner(a, b)

    print(foo(2, 7, f))
