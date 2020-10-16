# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Test\Code\Python\MachineLearning\Ui\ChildWidgt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChildWidgt(object):
    def setupUi(self, ChildWidgt):
        ChildWidgt.setObjectName("ChildWidgt")
        ChildWidgt.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(ChildWidgt)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(ChildWidgt)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)

        self.retranslateUi(ChildWidgt)
        QtCore.QMetaObject.connectSlotsByName(ChildWidgt)

    def retranslateUi(self, ChildWidgt):
        _translate = QtCore.QCoreApplication.translate
        ChildWidgt.setWindowTitle(_translate("ChildWidgt", "Form"))
