#импорт библиотек
#пример использования библиотеки easyGui
import easygui


#инициализация функции чтения
def read_file(name):
    with open(name, 'r', encoding='utf-8') as f:
        data = f.read()
    return data

#Основной цикл программы
while True:
    command = easygui.buttonbox('Хотите воспользоваться программой?', 'Главное окно', ['Да','Нет'])
    if command == 'Да':
        file_name = easygui.fileopenbox('Выбрать файл', 'Окно выбора')
        easygui.codebox(file_name, 'Просмотр файла', read_file(file_name))
    else:
        easygui.msgbox('Спасибо, что воспользовались программой!', 'Окно завершения программы')
        break




