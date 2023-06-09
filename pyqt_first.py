# -*- coding: utf-8 -*-
# @FileName :  pyqt_first.py
# @Author   : TianChao
# @Email    : tianchao0533@gamil.com
# @Time     :  2023/4/28 9:32
# @Software : PyCharm
# Description: 入门
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QDesktopWidget

if __name__ == "__main__":
	"""
	创建应用程序,只要是Qt制作的界面，有且只有一个QApplication对象
	sys.argv当做参数的目的是将运行时的命令参数传递给QApplication对象
	"""
	app = QApplication(sys.argv)

	w = QWidget()  # 创建窗口
	w.setWindowTitle('First PyQt')  # 设置窗口名字
	w.setWindowIcon(QIcon('icon09.png'))  # 设置窗口图标

	lbl = QLabel('ID', w)  # 创建文字标签，并设置父对象
	lbl.setGeometry(20, 20, 30, 20)  # 调整标签位置与大小，x,y,w,h

	eit = QLineEdit(w)  # 创建输入框并设置父对象
	eit.setPlaceholderText("Input ID")  # 设置输入框预输入内容
	eit.setGeometry(55, 20, 200, 20)  # 调整标签位置与大小，x,y,w,h

	btn = QPushButton("login", w)  # 创建按钮
	btn.setGeometry(50, 80, 70, 30)  # 调整标签位置与大小，x,y,w,h
	# btn.setParent(w)  # 设置父对象

	w.resize(300, 300)  # 重设窗口大小

	# 移动自定义组件到桌面中心
	center_point = QDesktopWidget().availableGeometry().center()  # 获取桌面组件-》获取桌面可用位置-》获取桌面中心位置坐标
	print(QDesktopWidget().availableGeometry())
	print(center_point)
	x = center_point.x()  # 获取桌面中心坐标X轴
	y = center_point.y()  # 获取桌面中心坐标y轴

	old_x, old_y, width, height = w.frameGeometry().getRect()  # 解包自定义组件的位置和大小
	print(w.frameGeometry())
	print(old_x, old_y, width, height)
	w.move(int(x - width / 2), int(y - height / 2))  # 移动组件到桌面中心坐标减去窗口大小的一半

	w.show()  # 显示窗口

	app.exec()  # 程序进入循环等待状态
