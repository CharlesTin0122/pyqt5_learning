# -*- coding: utf-8 -*-
# @FileName :  pyqt_03.py
# @Author   : TianChao
# @Email    : tianchao0533@gamil.com
# @Time     :  2023/4/26 11:20
# @Software : PyCharm
# Description: 信号连接

import sys
from functools import partial

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# import pymel.core as pm


# 槽函数
def fn():
	print(123)


def func(v):
	print(v)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	btn = QPushButton()

	# 不带参数
	btn.clicked.connect(fn)
	btn.clicked.connect(lambda: fn())
	btn.clicked.connect(partial(fn))
	# btn.clicked.connect(pm.callbacks(fn))

	# 带参数
	btn.clicked.connect(lambda: func(456))
	btn.clicked.connect(partial(func, 456))
	# btn.clicked.connect(pm.callbacks(func, 456))

	# 遍历使用
	# for i in range(5):
	# 	btn.clicked.connect(lambda: func(i))  # lambda槽函数遍历使用时可能会有问题

	for i in range(5):
		btn.clicked.connect(partial(func, i))

	btn.show()
	sys.exit(app.exec())
