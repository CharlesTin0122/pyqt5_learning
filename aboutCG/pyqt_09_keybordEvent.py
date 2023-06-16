# -*- coding: utf-8 -*-
# @FileName :  pyqt09_keybordEvent.py
# @Author   : TianChao
# @Email    : tianchao0533@gamil.com
# @Time     :  2023/6/16 15:46
# @Software : PyCharm
# Description:
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    """
    创建一个界面，用于显示键盘按键状态
    """
    def __init__(self):  # 构建函数
        super().__init__()  # 调用父类构建函数
        self.setWindowTitle("_________")
        self.resize(1, 1)
        self.lb1 = QLabel("按键Q状态： 抬起")
        self.lb2 = QLabel("按键W状态： 抬起")
        self.lb3 = QLabel("按键E状态： 抬起")

        self.setup_label(self.lb1)
        self.setup_label(self.lb2)
        self.setup_label(self.lb3)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        main_layout.addWidget(self.lb1)
        main_layout.addWidget(self.lb2)
        main_layout.addWidget(self.lb3)

    @staticmethod
    def setup_label(label):
        label.setFixedHeight(30)
        font = QFont()
        font.setPixelSize(30)
        label.setFont(font)

    def keyPressEvent(self, event) -> None:
        isAutoRepeat = event.isAutoRepeat()  # 该方法返回一个布尔值，判断按键是否长按
        if event.modifiers() & Qt.ShiftModifier:
            print("当前修饰键'shift'")
        if event.key() == Qt.Key_Shift:
            print("当前按下'shift'")

        if isAutoRepeat:
            if event.key() == Qt.Key_Q:
                self.lb1.setText("按键Q 状态：长按")
            elif event.key() == Qt.Key_W:
                self.lb2.setText("按键W 状态：长按")
            elif event.key() == Qt.Key_E:
                self.lb3.setText("按键E 状态：长按")
        else:
            if event.key() == Qt.Key_Q:
                self.lb1.setText("按键Q 状态：按下")
            elif event.key() == Qt.Key_W:
                self.lb2.setText("按键W 状态：按下")
            elif event.key() == Qt.Key_E:
                self.lb3.setText("按键E 状态：按下")

    def keyReleaseEvent(self, event) -> None:
        if event.key() == Qt.Key_Q:
            self.lb1.setText("按键Q 状态：抬起")
        elif event.key() == Qt.Key_W:
            self.lb2.setText("按键W 状态：抬起")
        elif event.key() == Qt.Key_E:
            self.lb3.setText("按键E 状态：抬起")


if __name__ == '__main__':  # 如果是本文件运行
    app = QApplication(sys.argv)  # 生成一个应用程序的实例，sys.argv为文件运行的参数列表
    w = MyWindow()  # 实例化自定义窗口
    w.show()  # 显示窗口
    sys.exit(app.exec())  # 让程序保持运行
