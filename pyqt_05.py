# -*- coding: utf-8 -*-
# @FileName :  pyqt_05.py
# @Author   : TianChao
# @Email    : tianchao0533@gamil.com
# @Time     :  2023/4/27 9:52
# @Software : PyCharm
# Description:相对布局

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

"""相对布局：随拖动窗口大小自适应"""


class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('LayOut')
		self.resize(800, 600)
		# 创建按钮
		button_1 = QPushButton("btn1")
		button_1.setStyleSheet('background:red')
		button_2 = QPushButton("btn2")
		button_2.setStyleSheet('background:blue')
		button_3 = QPushButton("btn3")
		button_3.setStyleSheet('background:green')
		button_4 = QPushButton("btn4")
		button_4.setStyleSheet('background:red')

		button_a = QPushButton("a")
		button_b = QPushButton("b")
		button_c = QPushButton("c")
		button_d = QPushButton("d")
		# 创建纵向布局,
		main_layout = QVBoxLayout()  # 创建纵向布局,V意为vertical，垂直
		main_layout.setSpacing(10)  # 按钮控件之间的距离
		main_layout.setContentsMargins(0, 0, 0, 0)  # 左上右下四个方向的边缘空隙
		self.setLayout(main_layout)  # 设置布局
		# 布局中添加按钮控件
		main_layout.addWidget(button_1)
		main_layout.addWidget(button_2)
		main_layout.addWidget(button_3)
		main_layout.addWidget(button_4)
		# 创建水平布局，并添加按钮控件
		sub_layout = QHBoxLayout()  # 创建水平布局，H意为horizontal，水平
		sub_layout.addWidget(button_a)
		sub_layout.addWidget(button_b)
		sub_layout.addWidget(button_c)
		sub_layout.addWidget(button_d)

		main_layout.addLayout(sub_layout)  # 设置sub_layout为main_layout的子布局

		# SpacerItem是一个空间空间，无内容用来填充空间，
		# 前两个参数是空间高度和宽度，后两个是宽度和高度的尺寸策略，
		# .Fixed:修复，部件宽度不能放大也不能缩小,.Expanding，扩展，部件高度将会得到尽可能多的空间
		main_layout.addSpacerItem(QSpacerItem(1, 1, QSizePolicy.Fixed, QSizePolicy.Expanding))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	print(sys.argv)
	w = MainWindow()
	w.show()
	sys.exit(app.exec_())

