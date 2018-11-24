from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

import sys


# Ui
from Ui.MainWindow import Ui_MainWindow

# 添加子窗口类
from ChildForm import CChildForm


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # 初始化子窗口
        self.cChildForm = CChildForm()

        # 添加子窗口
        self.ChildForm.addWidget(self.cChildForm)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    ui = MainWindow()
    ui.show()

    sys.exit(app.exec_())
