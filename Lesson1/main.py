#обычная функция
def print_text():
    name = input('Введите свое имя: ')
    print(f'Привет, {name}!')

print_text()

#функция принимающая
def summa(a,b):
    print(f'Сумма чисел: {a+b}')

num1 = int(input('Введи первое число: '))
num2 = int(input('Введи второе число: '))

summa(num1,num2)
summa(100, 57)

#функция возвращающая
def div(x,y):
    s = x/y
    return s

result = div(150, 25)
print(result)

#работа с файлами
file = open('test.txt', 'w')
file.write('ANDROMEDA')
file.close()
file = open('test.txt', 'r')
data = file.read()
file.close()

print(data)

#еще один способ работы с файлами
with open('test.txt', 'r') as file1:
    data1 = file1.read()
    print(data1)