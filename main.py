from app import MainWindow
from sys import argv
from PyQt6.QtWidgets import QApplication


def main():
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
