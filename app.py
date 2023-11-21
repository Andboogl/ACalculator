from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QKeySequence
import utils


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.operations = []

        # Design download
        self.design = utils.Ui_Form()
        self.design.setupUi(self)

        # Clicking on the buttons
        self.design.zero.clicked.connect(lambda: self.add_operation('0'))
        self.design.btn1.clicked.connect(lambda: self.add_operation('1'))
        self.design.btn2.clicked.connect(lambda: self.add_operation('2'))
        self.design.btn3.clicked.connect(lambda: self.add_operation('3'))
        self.design.btn4.clicked.connect(lambda: self.add_operation('4'))
        self.design.btn5.clicked.connect(lambda: self.add_operation('5'))
        self.design.btn6.clicked.connect(lambda: self.add_operation('6'))
        self.design.btn7.clicked.connect(lambda: self.add_operation('7'))
        self.design.btn8.clicked.connect(lambda: self.add_operation('8'))
        self.design.btn9.clicked.connect(lambda: self.add_operation('9'))

        self.design.float_number.clicked.connect(lambda: self.add_operation('.'))
        self.design.plus.clicked.connect(lambda: self.add_operation('+'))
        self.design.minus.clicked.connect(lambda: self.add_operation('-'))
        self.design.division.clicked.connect(lambda: self.add_operation('/'))
        self.design.multiplication.clicked.connect(lambda: self.add_operation('*'))
        self.design.bracket_to_right.clicked.connect(lambda: self.add_operation('('))
        self.design.bracket_to_left.clicked.connect(lambda: self.add_operation(')'))
        self.design.result.clicked.connect(self.get_sum)

        # Shortcuts
        self.design.zero.setShortcut(QKeySequence('0'))
        self.design.btn1.setShortcut(QKeySequence('1'))
        self.design.btn2.setShortcut(QKeySequence('2'))
        self.design.btn3.setShortcut(QKeySequence('3'))
        self.design.btn4.setShortcut(QKeySequence('4'))
        self.design.btn5.setShortcut(QKeySequence('5'))
        self.design.btn6.setShortcut(QKeySequence('6'))
        self.design.btn7.setShortcut(QKeySequence('7'))
        self.design.btn8.setShortcut(QKeySequence('8'))
        self.design.btn9.setShortcut(QKeySequence('9'))

        self.design.plus.setShortcut(QKeySequence('+'))
        self.design.minus.setShortcut(QKeySequence('-'))
        self.design.division.setShortcut(QKeySequence('/'))
        self.design.multiplication.setShortcut(QKeySequence('*'))
        self.design.float_number.setShortcut(QKeySequence('.'))
        self.design.result.setShortcut(QKeySequence('='))

        self.design.clear_btn.triggered.connect(self.clear)
        self.design.delete_symbol_btn.triggered.connect(self.delete_symbol)

    def clear(self):
        self.operations.clear()
        self.design.instance.setText('')

    def delete_symbol(self):
        try:
            self.operations.pop()
            text_to_set = self.design.instance.text()[0:-1]
            self.design.instance.setText(text_to_set)

        except IndexError:
            pass

    def add_operation(self, value):
        self.operations.append(value)
        self.design.instance.setText(''.join(self.operations))

    def get_sum(self):
        try:
            result = utils.get_sum(self.design.instance.text())
            self.design.instance.setText(str(result))

        except Exception as error:
            utils.show_message(self, f'Помилка обчислення ({error})')
