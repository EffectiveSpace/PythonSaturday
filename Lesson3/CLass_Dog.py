import random
class Dog:
    def __init__(self, name, color):
        self.name = name
        self.legs = 4
        self.color = color
        self.tricks = []

    def add_tricks(self, trick):
        self.tricks.append(trick)

    def do_tricks(self):
        if self.tricks:
            print(f'{self.name} сделал {random.choice(self.tricks)}')
        else:
            print(f'{self.name} не знает ниодного трюка')

Bob = Dog('BOB', 'braun')
Bob.add_tricks('кувырок')
Bob.do_tricks()
print(f'Цвет Boba {Bob.color}')

Palkan = Dog('Palkan','black')
Palkan.do_tricks()
