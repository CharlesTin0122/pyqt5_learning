# -*- coding: utf-8 -*-
# @FileName :  pyqt_12_Signal.py
# @Author   : TianChao
# @Email    : tianchao0533@gamil.com
# @Time     :  2023/6/16 17:26
# @Software : PyCharm
# Description:
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QWidget):
    mouse_pressed = pyqtSignal(int)

    def __init__(self):  # 构建函数
        super().__init__()  # 调用父类构建函数
        self.setWindowTitle("Python")
        self.resize(800, 600)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

    def mousePressEvent(self, event):
        e_btn = event.button()
        if e_btn == Qt.LeftButton:
            self.mouse_pressed.emit(0)
        elif e_btn == Qt.MiddleButton:
            self.mouse_pressed.emit(1)
        elif e_btn == Qt.RightButton:
            self.mouse_pressed.emit(2)


def print_mouse_info(enum):
    if enum == 0:
        print("Left")
    elif enum == 1:
        print("Middle")
    elif enum == 2:
        print("Right")


if __name__ == '__main__':  # 如果是本文件运行
    app = QApplication(sys.argv)  # 生成一个应用程序的实例，sys.argv为文件运行的参数列表
    w = MyWindow()  # 实例化自定义窗口
    w.mouse_pressed.connect(print_mouse_info)
    w.show()  # 显示窗口
    sys.exit(app.exec())  # 让程序保持运行
