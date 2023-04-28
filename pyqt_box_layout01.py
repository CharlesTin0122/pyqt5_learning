# -*- coding: utf-8 -*-
# @FileName :  pyqt_box_layout01.py
# @Author   : TianChao
# @Email    : tianchao0533@gamil.com
# @Time     :  2023/4/28 13:45
# @Software : PyCharm
# Description:盒子布局
import sys

from PyQt5.QtWidgets import *


class MainWindow(QWidget):
	def __init__(self):  # 构建函数
		super().__init__()  # 调用父类构建函数
		self.setWindowTitle('Vertical_LayOut')
		self.resize(300, 300)

		layout = QVBoxLayout()
		layout.addStretch(1)  # 为布局添加一个伸缩器（可以理解为一个弹簧，将部件顶起来），参数为比例关系

		bnt1 = QPushButton('button1')
		layout.addWidget(bnt1)
		bnt2 = QPushButton('button2')
		layout.addWidget(bnt2)
		bnt3 = QPushButton('button3')
		layout.addWidget(bnt3)

		layout.addStretch(2)  # 为布局添加一个伸缩器（可以理解为一个弹簧，将部件顶起来），参数为比例关系

		self.setLayout(layout)


if __name__ == '__main__':  # 如果是本文件运行
	app = QApplication(sys.argv)  # 生成一个应用程序的实例，sys.argv为文件运行的参数列表
	w = MainWindow()  # 实例化自定义窗口
	w.show()  # 显示窗口
	app.exec_()  # 让程序保持运行
