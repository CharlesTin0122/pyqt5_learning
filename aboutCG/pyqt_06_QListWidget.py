# -*- coding: utf-8 -*-
# @FileName :  pyqt_06.py
# @Author   : TianChao
# @Email    : tianchao0533@gamil.com
# @Time     :  2023/4/27 10:45
# @Software : PyCharm
# Description:自定义图片标签控件
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
"""-------------------------------自定义图片标签控件------------------------"""


class ImageLabel(QWidget):  # 创建图片文字标签类
	"""
	图片文字标签类：上面一个标签显示图片。下面一个标签显示文字，将两个标签放入一个垂直布局里
	因为每个图片文字标签类都有不同的图片和文字，所以引入图片和文字两个参数
	"""
	def __init__(self, tex, image_path):  # 构造函数，创建两个形参tex, image_path
		super().__init__()  # 调用父类构造函数
		lb_image = QLabel()  # 创建一个标签
		q_pixmap = QPixmap(image_path).scaled(100, 100)  # 创建一个像素图，并缩放大小到100*100像素
		lb_image.setPixmap(q_pixmap)  # 给标签设置图像
		lb_image.setAlignment(Qt.AlignHCenter)  # 使标签居中

		lb_text = QLabel()  # 创建一个标签
		lb_text.setText(tex)  # 设置标签文字
		lb_text.setAlignment(Qt.AlignHCenter)  # 使标签居中
		font = QFont()  # 设置一个字体
		font.setPixelSize(20)  # 设置字体像素大小
		lb_text.setFont(font)  # 设置标签字体大小

		main_layout = QVBoxLayout()  # 创建一个垂直布局
		main_layout.setContentsMargins(0, 0, 0, 0)  # 设置布局左上右下四个方向的边缘空隙
		self.setLayout(main_layout)  # 给实例设置布局
		main_layout.addWidget(lb_image)  # 给布局添加图片标签控件
		main_layout.addWidget(lb_text)  # 给布局添加文字标签控件

		self.setFixedSize(100, 100+30)  # 重设控件大小
		lb_text.setFixedSize(100, 30)  # 重设文字标签大小
		lb_image.setFixedSize(100, 100)  # 重设图片标签大小


class MainWindow(QWidget):
	"""
	创建主窗口类,结构为：
	QWidget-》QVBoxLayout-》QListWidget-》QListWidgetItem-》QVBoxLayout-》QLabel
	要注意的是QListWidget, QListWidgetItem,
	QListWidget.setItemWidget, QListWidget.addItem
	"""
	def __init__(self):
		super().__init__()
		self.setWindowTitle('——————')
		self.resize(800, 600)

		self.lw = QListWidget()  # 创建一个列表控件，QListWidget是一个窗体类，可以实现列表布局效果
		self.lw.setFlow(QListWidget.LeftToRight)  # 设置列表控件方向为从左至右
		self.lw.setWrapping(True)  # 设置列表控件为可换行
		self.lw.setResizeMode(QListWidget.Adjust)  # 设置列表控件为可自动调整位置
		# 遍历所有图片创建控件
		for i in range(9):
			self.add_item(f'widget{i+1}', f"icon0{i+1}.png")

		main_layout = QVBoxLayout()  # 创建垂直布局
		self.setLayout(main_layout)  # 设置布局
		main_layout.addWidget(self.lw)  # 布局中添加控件

	def add_item(self, text, image_path):
		imglb = ImageLabel(text, image_path)  # 实例化一个自定义控件
		item = QListWidgetItem()  # 实例化一个列表窗体项目
		item.setSizeHint(imglb.size())  # 设置项目尺寸和自定义控件一样大
		self.lw.addItem(item)  # 将项目添加到列表窗体中
		self.lw.setItemWidget(item, imglb)  # 把自定义控件指定给项目


if __name__ == '__main__':
	app = QApplication(sys.argv)
	print(sys.argv)
	w = MainWindow()
	w.show()
	sys.exit(app.exec())

"""
这段代码创建了一个图形用户界面窗口，其中包含一个列表，每个列表项都包含一个图像和文本。具体实现过程如下：
1. 代码导入了所需的PyQt5模块。
2. 定义了ImageLabel类，接受两个参数 - tex和image_path。该类创建了一个控件，其中包含一个文本标签和一个图像。它还将控件的大小设置为100x100，并将文本和图像的对齐方式设置为居中。
3. 定义了MainWindow类，创建了一个带有标题和列表控件的窗口。
4. 定义了add_item（）方法，接受两个参数 - text和image_path。该方法使用给定的参数创建ImageLabel类的实例，并将其添加到列表控件中。
5. 定义了主函数，创建了一个应用程序和一个MainWindow实例。然后显示窗口，并在关闭窗口时退出应用程序。
"""