import easygui as eg
value = eg.msgbox('Добро пожаловать в Андромеду', 'ANDROMEDA','Записаться',image='Andromeda.jpg')
if value == 'Записаться':
    name = eg.enterbox('Введите ваше имя', 'ОКНО ВВОДА')
    buttons = ['Ввести номер телефона','e-mail','загрузить скан паспорта']
    #eg.buttonbox(f'{name} выбери один из вариантов','ОКНО ВЫБОРА',choices=buttons)
    value = eg.choicebox(f'{name} выбери один из вариантов','ОКНО ВЫБОРА',choices=buttons)
    if value == 'загрузить скан паспорта':
        file = eg.fileopenbox('Выбрать файл','ОКНО ВЫБОРА')
        print(file)