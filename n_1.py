a = 13
b = 17
d = 10

c = a + b + d

print(c)
print(a,b,d,c)


time = int(input("введите время в секундах-"))
hours = time // 3600
minutes = (time // 60) - (hours * 60)
seconds = time % 60
print(f"{hours:02}):{minutes:02}:{seconds:02}")


n = input("введите положительное число-")
print(f"{n} + {n + n} + {n + n + n}) = {int(n) + int(n + n) + int(n + n + n)}")


num_init = int(input("введите целое положительное число -"))
maximum = num_init % 10
num = num_init

while num > 0:
    digit = num % 10
    if digit > maximum:
        maximum = digit

    if digit == 9:
            break
num //= 10
print(num)
print(f"наибольшая цифра в числе {num_init} равна {maximum}")




revenue = float(input("введите значение выручки-"))
costs = float(input("введите значение издержек-"))
result = revenue - costs

    if result > 0:
        print(f"Ваша фирма работает с прибылью {result}!")
        print(f"Рентабельность выручки-{result/revenue:.3f}")
        persons = int(input("Сколько сотрудников в компании ?-"))
        print(f"Прибыль на одного сотрудника-{result/persons:2f}")
    elif result < 0:
        print(f'Вы работаете с убытком-{-result}')
    else:
        print(f"Ноль- это тоже результат! Это стабильно!")



     while True :
         days = 1
         start_km = float(input("Начальный результат-"))
         target_km = float(input("Финальный результат-"))
         if start_km <= 0 or target_km < 0:
             print('Результаты должны быть больше нуля! Стартовое значение !=0')
         else:
               while start_km < target_km:
                   start_km *= 1.1
                   days += 1
               print(f"Спортсмен добьется результата за {days}дней")

















