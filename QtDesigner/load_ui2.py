import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


class MyWindow(QWidget):
    """
    调用ui文件进行操作
    """
    # 构建函数
    def __init__(self):
        super().__init__()
        self.text_browser = None
        self.cancel_btn = None
        self.login_btn = None
        self.pass_word = None
        self.user_name = None
        self.ui = None
        self.create_ui()

    def create_ui(self):
        """
        创建ui
        :return: None
        """
        self.ui = uic.loadUi("./login.ui")  # 调用ui文件
        print(self.ui)  # ui文件中的最顶层对象
        print(self.ui.__dict__)  # ui文件中的最顶层对象所有属性，键值对方式显示
        print(self.ui.label)  # ui文件中的最顶层对象嵌套的QLabel对象
        print(self.ui.label.text())  # ui文件中的最顶层对象嵌套的QLabel对象的文本
        # 获取所有ui文件中的嵌套对象
        self.user_name = self.ui.lineEdit
        self.pass_word = self.ui.lineEdit_2
        self.login_btn = self.ui.pushButton
        self.cancel_btn = self.ui.pushButton_2
        self.text_browser = self.ui.textBrowser
        # 给登录按钮设置槽函数
        self.login_btn.clicked.connect(self.login_btn_click)

    def login_btn_click(self):
        """
        登录按钮槽函数
        :return: None
        """
        user_name = self.user_name.text()
        password = self.pass_word.text()
        if user_name == "CharlesTin" and password == "880122":
            self.text_browser.setText(f"Welcome {user_name}...")
            self.text_browser.repaint()
        else:
            self.text_browser.setText("ID or Password error...")
            self.text_browser.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.ui.show()
    app.exec()
