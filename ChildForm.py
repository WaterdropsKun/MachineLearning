from PyQt5.QtWidgets import QWidget

from Ui.ChildWidgt import Ui_ChildWidgt


class CChildForm(QWidget, Ui_ChildWidgt):
    def __init__(self):
        super(CChildForm, self).__init__()
        self.setupUi(self)