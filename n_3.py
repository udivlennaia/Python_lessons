def season (m) :
    if m == 12 or m == 1 or m == 2:
        return'Это зима'
    elif m == 3 or m == 4 or m == 5:
         return 'Это весна'
    elif m == 6 or m == 7 or m == 8:
         return 'Это лето'
    elif m == 9 or m == 10 or m == 11:
        return 'Это осень'
    elif m == 0 or m > 12:
        return 'Нет такого месяца !'
result = season(int(input('Введите номер месяца:')))
print(result)


# решение нашла в сети - честно













# ввести значение