import lets_fly_with_me as lf


def test_function(x):
    sub_result = d * 100
    def inner_function(x):
        print('Я в области видимости функции test_function')
    inner_function(x)
    return sub_result

def usa_format(x):
    return '{:,}'.format(x)

d = 100

print(d)
res = test_function(5)
print(usa_format(res))

# res = inner_function(5)
# print(res)                  # вызов функции приводит к ошибке, т.к. функция находится встроенной в другую функцию и
                                # не является глобальной
