class NotDivideToZero(Exception):
    def __init__(self):
        self.txt = 'Нельзя делить на 0'


try:
    dividend = int(input('введите делимое: '))
    divider = int(input('введите делитель: '))
    if divider == 0:
        raise NotDivideToZero()
except NotDivideToZero as err:
    print(err.txt)

else:
    print(f'Реультат: {dividend / divider}')
