# -*- coding: utf-8 -*-
# @FileName :  pyqt_form_layout.py
# @Author   : TianChao
# @Email    : tianchao0533@gamil.com
# @Time     :  2023/4/28 15:45
# @Software : PyCharm
# Description: 表单布局
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):  # 构建函数
        super().__init__()  # 调用父类构建函数
        self.init_ui()  # 调用界面函数

    def init_ui(self):
        self.setFixedSize(300, 150)  # 禁止改变宽高（不可以拉伸）
        container = QVBoxLayout()  # 外层容器
        form_layout = QFormLayout()  # 表单容器

        edit = QLineEdit()  # 创建第一个输入框
        edit.setPlaceholderText("Please Input Your ID")  # 设置输入框预输入内容
        form_layout.addRow("ID", edit)  # 添加输入框到表单布局

        edit2 = QLineEdit()  # 创建第二个输入框
        edit2.setPlaceholderText("Please Input Your Password")  # 设置输入框预输入内容
        form_layout.addRow("Password", edit2)  # 添加输入框到表单布局
        # 将表单布局添加到外层容器垂直布局
        container.addLayout(form_layout)
        # 创建按钮，并设置大小不可拉伸
        login_btn = QPushButton("Login")
        login_btn.setFixedSize(100, 30)
        # 将按钮添加到外层容器布局，并指定对齐方式
        container.addWidget(login_btn, alignment=Qt.AlignRight)
        # 设置当前Widget的布局器，从而显示这个布局器中的子控件
        self.setLayout(container)


if __name__ == "__main__":  # 如果是本文件运行
    app = QApplication(sys.argv)  # 生成一个应用程序的实例，sys.argv为文件运行的参数列表
    w = MyWindow()  # 实例化自定义窗口
    w.show()  # 显示窗口
    app.exec()  # 让程序保持运行
