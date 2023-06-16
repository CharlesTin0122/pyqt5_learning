# -*- coding: utf-8 -*-
# @FileName :  test.py
# @Author   : TianChao
# @Email    : tianchao0533@gamil.com
# @Time     :  2023/4/26 10:20
# @Software : PyCharm
# Description: 界面和窗口
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Widget(QWidget):  # QWidget是PyQt中所有窗口类的基类，所有的控件和窗口都是通过其拓展出来的，实例化后生成空白窗体。
    def __init__(self):  # 构建函数
        super().__init__()  # 调用父类构建函数
        self.setWindowTitle("Main Window")  # 设置窗口标签
        self.resize(800, 600)  # 设置窗口大小
        self.move(0, 0)  # 移动窗口到左上角
        self.setGeometry(0, 0, 800, 600)  # 相当于move + resize
        self.setWindowIcon(QIcon("teGraphEditor.png"))  # 设置窗口图标
        self.setStyleSheet("background:rgb(100,200,200)")  # PyQt通过绘图事件和样式表的方式进行界面美化
        # 设置窗口旗标，置顶旗标，Qt类是一个枚举类，WindowStaysOnTopHint属性使窗口始终置顶
        self.setWindowFlags(Qt.WindowStaysOnTopHint)


if __name__ == "__main__":  # 如果是本程序运行
    app = QApplication(sys.argv)  # 生成一个QApplication（应用程序）的实例，使用PyQt必须生成，否则程序会崩溃
    print(sys.argv)  # 打印sys.argv，sys.argv是一个文件运行的参数列表
    w = Widget()  # 窗口类实例化
    # 打印一堆有的没的
    print(w.width())
    print(w.height())
    print(w.size())
    print(w.pos())
    print(w.styleSheet())

    w.show()  # 显示窗口 w.hind()：隐藏，w.close():关闭
    sys.exit(app.exec())  # app.exec()使app实例运行起来，sys.exit用来捕获程序的异常退出
