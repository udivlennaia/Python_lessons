def my_pow_fun(x, y):
    try:
        x, y = float(x),int(y)
        if x <= 0 or y >= 0:
            return 'Ошибка x должен быть больше 0,а y должен быть меньше 0'
        else:
            result = 1
            for _ in range(abc(y)):
                result *= 1/x
            return f'Результат возведения x в степень y: {round(result, 6)}'
    except ValueError:
        return "Программа работает только с числами ."

print(my_pow_fun(2, -3))

