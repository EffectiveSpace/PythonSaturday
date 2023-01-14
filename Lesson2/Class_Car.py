# Создание класса Car
# class Car:
#     speed = 250
#     color = 'red'
#     seats = 4
#     def beep(self):
#         print('BEEEEEP')
#
# Создание экземпляров класса Car
# porsche = Car()
# bmw = Car()
# fiat = Car()


# Вывод свойств и методов созданных экземляров
# print(f'Цвет машины - {porsche.color}')
# print(f'Скорость машины - {porsche.speed}')
# porsche.beep()
# bmw.beep()
# fiat.beep()

# Создание класса с конструктором __init__
class Car:
    def __init__(self, speed, color, seats):
        self.speed = speed
        self.color = color
        self.seats = seats
        self.wheel = 4
    def beep(self):
        print('BEEEEP')
    def say_speed(self):
        print(f'Скорость авто - {self.speed}')
    def say_color(self):
        print(f'Цвет авто - {self.color}')
    def say_seats(self):
        print(f'Кол-во мест в авто - {self.seats}')

#Создание экземпляра porsсhe класса Car со своими свойствами
porsсhe = Car(350,'red',2)
porsсhe.say_color()
porsсhe.say_speed()
porsсhe.say_seats()
print(porsсhe.wheel)

#Создание экземпляра bmw класса Car со своими свойствами
bmw = Car(260,'black', 6)
bmw.say_color()
bmw.say_speed()
bmw.say_seats()
print(bmw.wheel)
