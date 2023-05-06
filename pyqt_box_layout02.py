# -*- coding: utf-8 -*-
# @FileName :  pyqt_box_layout02.py.py
# @Author   : TianChao
# @Email    : tianchao0533@gamil.com
# @Time     :  2023/4/28 14:31
# @Software : PyCharm
# Description: 盒子布局
import sys

from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):  # 构建函数
        super().__init__()  # 调用父类构建函数
        self.init_ui()  # 调用界面函数

    def init_ui(self):
        container = QVBoxLayout()  # 最外层的垂直布局作为容器布局，包含两个部分
        hobby_box = QGroupBox('Hobby')  # 创建第一个组
        # 创建垂直布局
        v_layout = QVBoxLayout()
        # 创建按钮
        btn1 = QRadioButton('Smoking')
        btn2 = QRadioButton('Drinking')
        btn3 = QRadioButton('Gambling')
        # 为布局添加按钮
        v_layout.addWidget(btn1)
        v_layout.addWidget(btn2)
        v_layout.addWidget(btn3)
        # 为组设置布局
        hobby_box.setLayout(v_layout)
        # 创建第二个组
        gender_box = QGroupBox('sex')
        # 创建横向布局
        h_layout = QHBoxLayout()
        # 创建按钮
        btn4 = QRadioButton('Male')
        btn5 = QRadioButton('Female')
        # 为布局添加按钮
        h_layout.addWidget(btn4)
        h_layout.addWidget(btn5)
        # 为组设置布局
        gender_box.setLayout(h_layout)
        # 为容器布局添加组
        container.addWidget(hobby_box)
        container.addWidget(gender_box)
        # 设置布局为容器布局
        self.setLayout(container)


if __name__ == '__main__':  # 如果是本文件运行
    app = QApplication(sys.argv)  # 生成一个应用程序的实例，sys.argv为文件运行的参数列表
    w = MainWindow()  # 实例化自定义窗口
    w.show()  # 显示窗口
    app.exec()  # 让程序保持运行
