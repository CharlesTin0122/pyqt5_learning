# -*- coding: utf-8 -*-
# @FileName :  pyqt_09_dragEvent.py
# @Author   : TianChao
# @Email    : tianchao0533@gamil.com
# @Time     :  2023/6/16 16:14
# @Software : PyCharm
# Description:创建一个可拖拽图片并显示图片的标签和一个可拖拽文件并显示文件路径的文本框
import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Label(QLabel):
    """
    创建一个可拖拽图片并显示图片的标签类
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.resize(200, 200)
        self.setStyleSheet("background:rgb(100 ,100, 100)")
        self.setAcceptDrops(True)  # 将QLabel设置为可以拖拽

    def dragEnterEvent(self, event) -> None:
        """
        拖拽对象进入控件
        :param event: 拖拽事件
        :return: None
        """
        text = event.mimeData().text()  # 获取拖拽文件的文件路径：file:///G:/Code/pyqt5_study/icon01.png
        ext = os.path.splitext(text)[-1]  # 获取路径扩展名
        print(text)
        # 判断文件是否为图片，如果是，则开放拖拽事件
        if text.startswith("file:///") and ext in [".bmp", ".jpg", ".png"]:
            event.accept()

    def dropEvent(self, event) -> None:
        """
        在控件中释放对象
        :param event:
        :return: None
        """
        text = event.mimeData().text()
        path = text[8:]  # 获取文件可用路径，去除“file:///”
        # 通过路径设置图片，并设置图片的大小为标签大小，Qt.KeepAspectRatio参数保持宽高比
        self.setPixmap(QPixmap(path).scaled(self.size(), Qt.KeepAspectRatio))  # Qt.KeepAspectRatio保持宽高比


class LineEdit(QLineEdit):
    """
    一个可拖拽文件并显示文件路径的文本框类
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.resize(100, 30)
        self.setStyleSheet("background:rgb(100 ,100, 100)")

    def dragEnterEvent(self, event) -> None:
        """
        拖拽对象进入控件
        :param event: 拖拽事件
        :return: None
        """
        super().dragEnterEvent(event)  # 获取父类的拖拽函数dragEnterEvent
        text = event.mimeData().text()
        print(text)
        # 判断返回的文本是否为file开头，如果是，则开放拖拽事件
        if text.startswith("file:///"):
            event.accept()

    def dragMoveEvent(self, event) -> None:
        """
        拖拽对象在控件中移动
        :param event: 拖拽事件
        :return: None
        """
        pass

    def dragLeaveEvent(self, event) -> None:
        """
        拖拽对象离开控件
        :param event: 拖拽事件
        :return: None
        """
        pass

    def dropEvent(self, event) -> None:
        """
        在控件中释放对象
        :param event:
        :return: None
        """

        text = event.mimeData().text()
        # 判断返回的文本是否为file开头，如果是，则开放拖拽事件，如果否，则继承父类拖拽函数，实现文本拖拽功能
        if text.startswith("file:///"):
            self.setText(text[8:])
        else:
            super().dropEvent(event)


class MyWindow(QWidget):
    def __init__(self):  # 构建函数
        super().__init__()  # 调用父类构建函数
        self.setWindowTitle("...")
        self.resize(500, 400)
        line = LineEdit(self)
        label = Label(self)
        line.setGeometry(0, 0, 500, 30)
        label.setGeometry(120, 100, 200, 200)


if __name__ == '__main__':  # 如果是本文件运行
    app = QApplication(sys.argv)  # 生成一个应用程序的实例，sys.argv为文件运行的参数列表
    w = MyWindow()  # 实例化自定义窗口
    w.show()  # 显示窗口
    sys.exit(app.exec())  # 让程序保持运行
