class NotNumericElement(Exception):
    def __init__(self):
        self.txt = 'вводимый символ должен быть числом'


array = []
while True:
    value = input('введите число: ')
    is_numeric = value.isnumeric()
    if value == 'stop':
        print(array)
        break

    else:
        try:
            if not is_numeric:
                raise NotNumericElement
        except NotNumericElement as err:
            print(err.txt)
        else:
            array.append(value)
