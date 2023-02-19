import easygui as gui


def do_action(msg, title, valuta):
    value = gui.choicebox(msg, title, valuta)
    return value
