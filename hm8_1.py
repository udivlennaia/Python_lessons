class Date:
    date = None
    day = None
    month = None
    year = None

    def __init__(self, date):
        self.__class__.date = date

    def __str__(self):
        return self.date

    @classmethod
    def to_int(cls):
        date = [int(s) for s in cls.date.split('-')]
        cls.day = date[0]
        cls.month = date[1]
        cls.year = date[2]
        print(cls.day, cls.month, cls.year)

    @staticmethod
    def validate(d):
        if d.month > 12 or d.month < 1:
            raise Exception('Месяц должен быть от 1 до 12')


d = Date('2-1-2022')
d.to_int()
Date.validate(d)
