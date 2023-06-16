# -*- coding: utf-8 -*-
# @FileName :  pyqt_07_mouseEvent.py
# @Author   : TianChao
# @Email    : tianchao0533@gamil.com
# @Time     :  2023/6/16 13:53
# @Software : PyCharm
# Description:鼠标事件
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mouse Evant")
        self.resize(800, 600)
        self.setMouseTracking(True)

    def mousePressEvent(self, event) -> None:
        print("clicked Mouse")
        if event.button() == Qt.LeftButton:
            print("Clicked Mouse Left Button")
        elif event.button() == Qt.RightButton:
            print("Clicked Mouse Right Button")
        elif event.button() == Qt.MiddleButton:
            print("Clicked Mouse Middle Button")
        # &:与，两个位都为1时，结果才为1，Modifier为修饰键：ctrl,alt,shift
        if event.modifiers() & Qt.ControlModifier:
            print("Pushed Ctrl Button")
        if event.modifiers() & Qt.ShiftModifier:
            print("Pushed Shift Button")

    def mouseMoveEvent(self, event) -> None:
        print("Mouse Moved")
        if event.button() == Qt.LeftButton:
            print("Mouse Moved, Click Mouse Left Button")
        elif event.button() == Qt.RightButton:
            print("Mouse Moved, Click Mouse Right Button")
        elif event.button() == Qt.MiddleButton:
            print("Mouse Moved, Click Mouse Middle Button")
        # &:与，两个位都为1时，结果才为1
        if event.button() & Qt.LeftButton:
            print("Mouse Moved, Clicked Mouse Left Button")
        if event.button() & Qt.RightButton:
            print("Mouse Moved, Clicked Mouse Right Button")
        if event.button() & Qt.MiddleButton:
            print("Mouse Moved, Clicked Mouse Middle Button")

    def mouseReleaseEvent(self, event) -> None:
        print("Mouse Released")
        if event.button() == Qt.LeftButton:
            print("Released Left Button")
        elif event.button() == Qt.RightButton:
            print("Released Right Button")
        elif event.button() == Qt.MiddleButton:
            print("Released Middle Button")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
