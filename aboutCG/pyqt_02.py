# -*- coding: utf-8 -*-
# @FileName :  pyqt_02.py
# @Author   : TianChao
# @Email    : tianchao0533@gamil.com
# @Time     :  2023/4/26 10:42
# @Software : PyCharm
# Description: 按钮和标签

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


# 创建按钮类
class Button(QPushButton):

	def __init__(self):
		super().__init__()

		self.setText('OK')  # 设置按钮文本
		self.setIcon(QIcon('teGraphEditor.png'))  # 设置按钮图标
		self.clicked.connect(self.print123)  # 设置按钮点击
		self.clicked.connect(lambda: print(456))  # 设置按钮点击

		print(self.text())

	# 设置按钮点击函数
	@staticmethod
	def print123(self):
		print(123)


# 创建标签类
class Label(QLabel):
	def __init__(self):
		super().__init__()
		self.setText('Big Label')  # 设置标签文本
		# 设置标签居中，垂直居中，水平居中，“|”按位数或运算，两个位只要有一个为1，其值为1
		self.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		self.setPixmap(QPixmap('teGraphEditor.png'))  # 设置标签像素图，设置了像素图就不会显示文本


if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = Label()
	w.show()
	sys.exit(app.exec_())
