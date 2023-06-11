# -*- coding: utf-8 -*-
# @FileName :  pyqt_signal_slot.py
# @Author   : TianChao
# @Email    : tianchao0533@gamil.com
# @Time     :  2023/6/9 17:46
# @Software : PyCharm
# Description:
"""
点击按钮
->触发check_click槽函数
->槽函数中自定义信号发射信息
->触发my_slot槽函数
->my_slot槽函数收集并打印信息到标签
"""
import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    """
    滚动窗口，滚动显示信息
    """
    my_signal = pyqtSignal(str)  # 设置自定义信号，只能放在函数的外面,信号类型为字符串

    # 类的构建函数
    def __init__(self):
        super().__init__()  # 调用父类构建函数
        self.msg = None
        self.msg_history = list()  # 用来存放信息历史
        self.create_ui()

    # 构建UI
    def create_ui(self):
        self.resize(500, 200)  # 重定义窗口大小
        container = QVBoxLayout()  # 创建一个整体布局器

        self.msg = QLabel("")  # 创建空标签，用来显示检测到漏洞的信息
        self.msg.resize(440, 15)  # 重定义标签大小
        self.msg.setWordWrap(True)  # # 自动换行
        self.msg.setAlignment(Qt.AlignTop)  # 标签位置靠上

        scroll = QScrollArea()  # 创建滚动组件
        scroll.setWidget(self.msg)  # 将标签装进滚动组件

        v_layout = QVBoxLayout()  # 创建垂直布局器，用来添加自动滚动条
        v_layout.addWidget(scroll)  # 将滚动标签装进垂直布局器

        h_layout = QHBoxLayout()  # 创建水平布局器
        btn = QPushButton("Start Checking", self)  # 创建按钮

        btn.clicked.connect(self.check_click)  # 按钮点击信号连接槽函数，点击按钮则开始检测

        h_layout.addStretch(1)  # 水平布局器创建拉伸空间
        h_layout.addWidget(btn)  # 水平布局器添加按钮
        h_layout.addStretch(1)  # 水平布局器创建拉伸空间

        # 操作将要显示的控件以及子布局器添加到container
        container.addLayout(v_layout)  # 容器布局器添加垂直布局
        container.addLayout(h_layout)  # 容器布局器添加水平布局

        self.setLayout(container)  # 当前窗口添加总布局器

        self.my_signal.connect(self.my_slot)  # 自定信号连接槽函数

    # 创建点击按钮的槽函数
    def check_click(self):
        # 通过枚举循环生成文本mes
        for i, ip in enumerate([f"192.169.1.{x}" for x in range(1, 255)]):
            msg = f"模拟， 正在检查{ip}上的漏洞"
            # 通过索引模5是否余0 判断是否添加"发现漏洞"信息
            if (i+1) % 5 == 0:
                self.my_signal.emit(msg + "->发现漏洞")  # 如果判断成立，则自定义信号发射
                time.sleep(0.01)
            # else:
            #     self.my_signal.emit(msg)  # 如果判断成立，则自定义信号发射，对象.信号.发射(参数)
            #     time.sleep(0.01)

    # 创建自定义信号槽函数
    def my_slot(self, msg):
        print(msg)
        self.msg_history.append(msg)  # 将每条msg添加到msg_history
        self.msg.setText("\n".join(self.msg_history))  # 给标签设置文本为换行的msg_history
        self.msg.resize(400, self.msg.frameSize().height() + 15)  # 重定义标签大小，宽度不变，高度每次增加15
        self.msg.repaint()  # 每次都重画标签


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec()
