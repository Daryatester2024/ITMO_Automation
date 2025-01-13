class Car:

    def __init__(self, color:str, type:str, year:int):
        self.color=color
        self.type=type
        self.year=year

    def start (self):
        return 'Автомобиль заведён - {} '. format (self.type) + format (self.color) + format (self.year)

    def stop (self):
        return 'Автомобиль заглушен - {} '.format(self.type)

    def car_age(self):
        return 'год сборки автомобиля - {}'.format(self.year)

    def car_color (self):
        return 'цвет автомобиля - {}'.format(self.color)

    def car_type(self):
        return 'тип автомобиля - {}'.format(self.type)

car_1=Car('red', 'mazda',  2019)

print(car_1.start())

print(car_1.stop())

print(car_1.car_age())

print(car_1.car_type())

print(car_1.car_color())