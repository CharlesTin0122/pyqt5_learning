# -*- coding: utf-8 -*-
# @FileName :  pyqt_box_grid_layout.py.py
# @Author   : TianChao
# @Email    : tianchao0533@gamil.com
# @Time     :  2023/4/28 15:00
# @Software : PyCharm
# Description: 网格布局
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyWindow(QWidget):
	def __init__(self):  # 构建函数
		super().__init__()  # 调用父类构建函数
		self.init_ui()  # 调用界面函数

	def init_ui(self):  # 创建界面函数
		self.setWindowTitle('calculator')  # 设置窗体标题
		# 设置按钮数据
		data = {
			0: ["7", "8", "9", "+", "("],
			1: ["4", "5", "6", "-", ")"],
			2: ["1", "2", "3", "*", "<-"],
			3: ["0", ".", "=", "/", "C"]
		}

		layout = QVBoxLayout()  # 创建纵向布局

		edit = QLineEdit()  # 创建输入框
		edit.setPlaceholderText('Please Input')  # 设置输入框预输入内容
		layout.addWidget(edit)  # 将输入框添加到布局

		grid = QGridLayout()  # 创建网格布局
		# 遍历按钮数据依次创建按钮，并添加到网格布局中
		for line_number, line_list in data.items():
			for col_number, dat in enumerate(line_list):
				btn = QPushButton(dat)
				grid.addWidget(btn, line_number, col_number)
		# 纵向布局添加网格布局
		layout.addLayout(grid)
		# 设置布局为纵向布局
		self.setLayout(layout)


if __name__ == '__main__':  # 如果是本文件运行
	app = QApplication(sys.argv)  # 生成一个应用程序的实例，sys.argv为文件运行的参数列表
	w = MyWindow()  # 实例化自定义窗口
	w.show()  # 显示窗口
	app.exec()  # 让程序保持运行
