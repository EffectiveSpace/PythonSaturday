#загрузка необходимых модулей
from message import get_message
from action import do_action
from enter import do_enter

#Основная логика программы
msg_hello = 'Добро пожаловать в приложение "Конвертор валют"'
title_hello = 'ОКНО ПРИВЕТСТВИЯ'
button_list = ['Продолжить','Конвертировать']

VALUTA = ['DOLL', 'EUR', 'DH', 'RUP']
msg_choice = 'Выберите нужную валюту'
title_choice = 'ОКНО ВЫБОРА ВАЛЮТЫ'

msg_enter = 'Введите кол-во рублей'
title_enter = 'ОКНО ВВОДА'

k = [74, 79, 65, 50]

msg_answer = 'Результат расчета'
title_answer = 'ОКНО РЕЗУЛЬТАТА'

def run():
    while True:
        user = get_message(msg_hello, title_hello, button_list[0])
        if user:
            valuta = do_action(msg_choice, title_choice, VALUTA)
        else:
            get_message('До новых встреч', 'ОКНО ПРОЩАНИЯ','Выйти')
            break
        if valuta == 'DOLL':
            rub = do_enter(msg_enter, title_enter)
            doll = rub/k[0]
            get_message(msg_answer+f': {rub}руб. -> {round(doll)}$',title_answer, 'OK')


run()