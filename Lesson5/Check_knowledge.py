#Проверка кода программ:
#1 - функции и работа с файлами
#a - функция, записывающая числа от 50 до 65 включительно в текстовый файл (числа должны быть в каждой строке)
# def write_number():
#     open('num', 'r') as f:
#         for i in range():
#             f.write(i)
# write_number()

#b - функция, добавляющая к существующим числам - строку 'we are checking our knowledge'
# append_string():
#     with open('.txt', 'w') as file:
#         write(We are checking our knowledge)
#
# append_string()

#c - функция, читающая весь текст внутри файла num.txt и выводящая его в терминал
# def read_text():
#     with open('', '') as f:
#         f.read()
#     return data
#
# print(read_text)

#2 - ООП. Создание классов, их атребуты и методы
#a - класс Дом с атрибутами (используя конструктор __init__) и методами
# class Home:
#     __init__(self, name, floors, material, roof):
#         self.name = name
#         self.floors = floors
#         self.material = material
#         roof = roof
#
#     def keep_warm():
#         print(f'Дом {self.name} очень теплый!')
#
# house_1 = Home('Savin-House', 15, 'кирпич')
# print(f'В {house_1.name} сделан из {house_1.material}, в нем {house_1.floors} этажей')
# print(f'и {house_1.roof} крыша')
# house_1.keep_warm()

#Понятие наследования
# class Animals:
#     def __init__(self, teeth, color):
#         self.legs = 4
#         self.teeth = teeth
#         self.color = color
#
#     def jump(self):
#         print('Животное может прыгать')
#
# class HomeAn(Animals):
#     def __init__(self, teeth, color, name):
#         super().__init__(teeth, color)
#         self.name = name
#     def may(self):
#         super().jump()
#         print(f'Кошка {self.name} сказала мяу')
#
# cat = HomeAn(36, 'black', 'Ласка')
# cat.may()
#cat.jump()

