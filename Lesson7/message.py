import easygui as gui


def get_message(msg, title, button):
    flag = gui.msgbox(msg,title, button)
    return flag