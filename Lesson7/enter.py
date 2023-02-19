import easygui as gui


def do_enter(msg, title):
    rub = int(gui.enterbox(msg, title))
    return rub