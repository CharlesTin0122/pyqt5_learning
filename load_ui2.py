import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = None
        self.create_ui()

    def create_ui(self):
        self.ui = uic.loadUi("./login.ui")
        print(self.ui.__dict__)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.ui.show()
    app.exec()
