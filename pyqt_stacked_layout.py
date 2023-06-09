# -*- coding: utf-8 -*-
# @FileName :  pyqt_stacked_layout.py
# @Author   : TianChao
# @Email    : tianchao0533@gamil.com
# @Time     :  2023/4/28 16:04
# @Software : PyCharm
# Description: 堆叠布局
import sys

from PyQt5.QtWidgets import *


# 创建堆叠布局中所用的标签组件的类
class Win(QWidget):
    def __init__(self, text, sheet):
        super().__init__()
        self.text = text  # 设置标签所需的文本变量
        self.sheet = sheet  # 设置标签所需的样式表变量
        stacked_label = QLabel(self.text, self)  # 创建标签
        stacked_label.setStyleSheet(self.sheet)  # 设置标签样式表


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.stacked_layout = None  # 构建时创建变量
        self.create_stacked_layout()  # 构建时运行函数
        self.init_ui()  # 构建时运行函数

    def create_stacked_layout(self):  # 创建堆叠布局函数
        # 创建堆叠(抽屉)布局
        self.stacked_layout = QStackedLayout()  # 创建堆叠布局
        # 创建单独的Widget
        win1 = Win("我是抽屉1要显示的内容", "background-color:green;")  # 创建堆叠布局所用的标签组件
        win2 = Win("我是抽屉2要显示的内容", "background-color:red;")  # 创建堆叠布局所用的标签组件
        # 将创建的2个标签组件添加到堆叠布局器中
        self.stacked_layout.addWidget(win1)
        self.stacked_layout.addWidget(win2)

    def init_ui(self):  # 构建主窗口函数
        self.setFixedSize(300, 270)  # 设置Widget大小以及固定宽高
        container = QVBoxLayout()  # 1. 创建整体的容器布局器

        # 2. 创建1个要显示具体内容的子Widget
        widget = QWidget()
        widget.setLayout(self.stacked_layout)
        widget.setStyleSheet("background-color:grey;")

        # 3. 创建2个按钮，用来点击进行切换抽屉布局器中的Widget
        btn_press1 = QPushButton("抽屉1")
        btn_press2 = QPushButton("抽屉2")

        # 绑定信号和槽函数：对象.信号.connect(槽函数)
        btn_press1.clicked.connect(self.btn_press1_clicked)  # 给按钮添加事件（即点击后要调用的函数）
        btn_press2.clicked.connect(self.btn_press2_clicked)  # 给按钮添加事件（即点击后要调用的函数）

        # 4. 将需要显示的空间添加到布局器中
        container.addWidget(widget)
        container.addWidget(btn_press1)
        container.addWidget(btn_press2)

        # 5. 设置当前要显示的Widget，从而能够显示这个布局器中的控件
        self.setLayout(container)

    def btn_press1_clicked(self):
        # 设置抽屉布局器的当前索引值，即可切换显示哪个Widget
        self.stacked_layout.setCurrentIndex(0)

    def btn_press2_clicked(self):
        # 设置抽屉布局器的当前索引值，即可切换显示哪个Widget
        self.stacked_layout.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = MyWindow()
    win.show()

    app.exec()
