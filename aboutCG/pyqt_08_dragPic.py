# -*- coding: utf-8 -*-
# @FileName :  pyqt_08_dragPic.py
# @Author   : TianChao
# @Email    : tianchao0533@gamil.com
# @Time     :  2023/6/16 14:48
# @Software : PyCharm
# Description:
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

"""

event.button() 和 event.buttons() 是 PyQt5 中用于处理鼠标事件的两个不同方法。

event.button()

event.button() 返回的是一个整数，表示触发鼠标事件的按钮。常见的返回值包括：
Qt.LeftButton：表示左键
Qt.RightButton：表示右键
Qt.MiddleButton：表示中键
Qt.XButton1 和 Qt.XButton2：表示额外的鼠标按钮（通常是鼠标上的前进和后退按钮）
当你只关心一个鼠标按钮的事件时，可以使用 event.button() 来判断触发事件的是哪个按钮。
event.buttons()

event.buttons() 返回的是一个整数，表示当前鼠标的按钮状态。可以通过对返回值进行位运算来判断是否按下了某个特定的按钮。
返回值是一个按位组合的标志位，表示当前按下的鼠标按钮。常见的标志位包括：
Qt.LeftButton：表示左键被按下
Qt.RightButton：表示右键被按下
Qt.MiddleButton：表示中键被按下
Qt.XButton1 和 Qt.XButton2：表示额外的鼠标按钮被按下
使用 event.buttons() 可以同时检查多个鼠标按钮的状态，例如判断同时按下左键和右键的情况。
总结：

event.button() 返回的是当前触发鼠标事件的按钮。
event.buttons() 返回的是当前鼠标的按钮状态。
函数返回当前按下的所有按钮，按钮状态可以是Qt::LeftButton,Qt::RightButton,Qt::MidButton或运算组合。
"""


class MyLabel(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.last_mouse_g_pose = None

    def mousePressEvent(self, event):
        """
        当鼠标点击时，将鼠标位置存入last_mouse_g_pose变量
        :param event: 鼠标点击事件
        :return: None
        """
        if event.button() == Qt.LeftButton:
            self.last_mouse_g_pose = QCursor.pos()  # QCursor.pos()获取鼠标在整个屏幕空间中的位置
            print(self.last_mouse_g_pose)

    def mouseMoveEvent(self, event):
        """
        移动鼠标，鼠标会处于一个新位置，新位置存入g_pos，新位置和旧位置之间的差存入delta_pose。
        标签原来的位置加上得到的位置差得到标签新的位置，就达到了鼠标拖动标签移动的效果
        移动完标签后，保存最新的鼠标位置到last_mouse_g_pose，这样在下次鼠标移动的会得到一个新的位置差
        注意：此时用的是event.buttons()，返回的是当前鼠标的按钮状态。包括鼠标的点击和移动。
        :param event:鼠标移动事件
        :return:None
        """
        if event.buttons() == Qt.LeftButton:
            g_pos = QCursor.pos()
            delta_pose = g_pos - self.last_mouse_g_pose
            self.move(self.pos() + delta_pose)
            self.last_mouse_g_pose = g_pos
            print("self.last_mouse_g_pose")


class MyWindow(QWidget):
    def __init__(self):  # 构建函数
        super().__init__()  # 调用父类构建函数
        self.setWindowTitle("______")
        self.resize(800, 600)
        self.lb = MyLabel(self)
        self.lb.setGeometry(50, 50, 50, 50)
        self.lb.setFixedSize(50, 50)
        self.lb.setStyleSheet("background:rgb(100, 0, 0)")


if __name__ == '__main__':  # 如果是本文件运行
    app = QApplication(sys.argv)  # 生成一个应用程序的实例，sys.argv为文件运行的参数列表
    w = MyWindow()  # 实例化自定义窗口
    w.show()  # 显示窗口
    sys.exit(app.exec())  # 让程序保持运行
"""
这里重点关注鼠标点击、释放、移动三个时间的具体实现，
if条件判断的是事件是否由鼠标左键触发，但若三个条件全部写成ev->button() == Qt::LeftButton，在运行的时候会发现，
只有鼠标的点击和释放方法真正的打印了其中的内容，移动事件不做出反应。
解决的方法是将原本的条件改为ev->buttons() == Qt::LeftButton这样，在点击鼠标左键后进行移动，就会有内容打印出来。
这是因为button()仅仅返回的是触发事件时的按键，而buttons()返回的是鼠标的状态，包括鼠标左中右三键的联合信息。

再者，使用ev->buttons() == Qt::LeftButton作为鼠标移动的判断条件时，
若鼠标左键按下并移动一段距离后再同时按下鼠标右键，继续移动鼠标发现又无法正常打印其内容，
解决方案是使用ev->buttons() & Qt::LeftButton来替换原来的条件，&在这里起到的作用是判断目前鼠标的联合状态中是否包含了鼠标左键，
这样，同时按下左右键再移动鼠标，就会有正常的文字输出了。
"""