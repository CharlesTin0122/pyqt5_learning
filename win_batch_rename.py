# -*- coding: utf-8 -*-
# Python 3.9 +
import os
import re
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class BatchRename(QWidget):
    def __init__(self):  # 构建函数
        super().__init__()  # 调用父类构建函数
        self.creat_ui()  # 调用界面函数

    def creat_ui(self):
        self.setFixedSize(300, 150)  # 禁止改变宽高（不可以拉伸）
        container = QVBoxLayout()  # 外层容器
        form_layout = QFormLayout()  # 表单容器

        edit = QLineEdit()  # 创建第一个输入框
        edit.setPlaceholderText("Input Your Path")  # 设置输入框预输入内容
        form_layout.addRow("Path", edit)  # 添加输入框到表单布局

        edit2 = QLineEdit()  # 创建第二个输入框
        edit2.setPlaceholderText("Input Your Replace String")  # 设置输入框预输入内容
        form_layout.addRow("Replace String", edit2)  # 添加输入框到表单布局

        edit3 = QLineEdit()  # 创建第二个输入框
        edit3.setPlaceholderText("Input Your Old String")  # 设置输入框预输入内容
        form_layout.addRow("Old String", edit3)  # 添加输入框到表单布局

        # 将表单布局添加到外层容器垂直布局
        container.addLayout(form_layout)
        # 创建按钮，并设置大小不可拉伸
        login_btn = QPushButton("batch Raname")
        login_btn.setFixedSize(100, 30)
        # 将按钮添加到外层容器布局，并指定对齐方式
        container.addWidget(login_btn, alignment=Qt.AlignRight)
        # 设置当前Widget的布局器，从而显示这个布局器中的子控件
        self.setLayout(container)



    # def batch_rename(self, replace_str: str, find_str: str, path: str) -> list:
    #     """
    #     批量修改替换文件名
    #     Args:
    #         replace_str: 要替换的字符串
    #         find_str: 原始字符串
    #         path: 要重命名的文件所在路径

    #     Returns:重命名后的名称列表

    #     """
    #     all_renamed_path = []  # 创建变量用来储存要返回的重命名后名称列表
    #     # 遍历整个路径，找到所有文件路径
    #     for root, dirs, files in os.walk(path):
    #         for filename in files:
    #             file_path = os.path.join(root, filename)
    #             # 正则表达式文件名重命名，注意这里的参数是：1.要替换的字符换，2.原始字符串，3.要修改的文件名
    #             renamed_filename = re.sub(replace_str, find_str, filename)
    #             renamed_path = os.path.join(root, renamed_filename)  # 将文件名重新组合成完整路径
    #             all_renamed_path.append(renamed_path)  # 将所完整路径添加到变量，用于返回
    #             # 重命名
    #             try:
    #                 os.rename(file_path, renamed_path)
    #                 print(f"Renamed: {file_path} -> {renamed_path}")
    #             except OSError as e:
    #                 print(f"Error renaming {file_path}: {e}")
    #     return all_renamed_path


if __name__ == "__main__":  # 如果是本文件运行
    app = QApplication(sys.argv)  # 生成一个应用程序的实例，sys.argv为文件运行的参数列表
    w = BatchRename()  # 实例化自定义窗口
    w.show()  # 显示窗口
    app.exec()  # 让程序保持运行