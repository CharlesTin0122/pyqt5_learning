# -*- coding: utf-8 -*-
# @FileName :  pyqt_04.py
# @Author   : TianChao
# @Email    : tianchao0533@gamil.com
# @Time     :  2023/4/27 9:39
# @Software : PyCharm
# Description:绝对布局
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

"""------------------------------------绝对布局---------------------------------------"""
# 不会随拖动窗口大小自适应


class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.resize(800, 600)

		button_1 = QPushButton("btn1", parent=self)
		button_1.move(0, 0)
		button_2 = QPushButton("btn2", parent=self)
		button_2.move(0, 100)
		button_3 = QPushButton("btn3", parent=self)
		button_3.move(200, 100)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = MainWindow()
	w.show()
	sys.exit(app.exec_())

