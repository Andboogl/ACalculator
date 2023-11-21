from PyQt6.QtWidgets import QMessageBox


def get_sum(instance):
    return eval(instance)


def show_message(window, msg):
    message = QMessageBox(window)
    message.setText(msg)
    message.exec()
