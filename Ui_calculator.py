# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\workspace\calculator\calculator.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore,  QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(532, 268)
        Dialog.setSizeGripEnabled(True)
        self.pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_1.setGeometry(QtCore.QRect(50, 90, 75, 23))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 90, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 90, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 130, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 130, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(230, 130, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 170, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(140, 170, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(230, 170, 75, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_0 = QtWidgets.QPushButton(Dialog)
        self.pushButton_0.setGeometry(QtCore.QRect(140, 210, 75, 23))
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_dot = QtWidgets.QPushButton(Dialog)
        self.pushButton_dot.setGeometry(QtCore.QRect(50, 210, 75, 23))
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.pushButton_equ = QtWidgets.QPushButton(Dialog)
        self.pushButton_equ.setGeometry(QtCore.QRect(410, 90, 75, 141))
        self.pushButton_equ.setObjectName("pushButton_equ")
        self.pushButton_div = QtWidgets.QPushButton(Dialog)
        self.pushButton_div.setGeometry(QtCore.QRect(320, 130, 75, 23))
        self.pushButton_div.setObjectName("pushButton_div")
        self.pushButton_mul = QtWidgets.QPushButton(Dialog)
        self.pushButton_mul.setGeometry(QtCore.QRect(320, 170, 75, 23))
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.pushButton_add = QtWidgets.QPushButton(Dialog)
        self.pushButton_add.setGeometry(QtCore.QRect(320, 210, 75, 23))
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_sub = QtWidgets.QPushButton(Dialog)
        self.pushButton_sub.setGeometry(QtCore.QRect(230, 210, 75, 23))
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.pushButton_cls = QtWidgets.QPushButton(Dialog)
        self.pushButton_cls.setGeometry(QtCore.QRect(320, 90, 75, 21))
        self.pushButton_cls.setObjectName("pushButton_cls")
        self.lcd = QtWidgets.QLCDNumber(Dialog)
        self.lcd.setDigitCount(10)
        self.lcd.setGeometry(QtCore.QRect(50, 10, 431, 61))
        self.lcd.setObjectName("lcd")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_1.setText(_translate("Dialog", "1"))
        self.pushButton_2.setText(_translate("Dialog", "2"))
        self.pushButton_3.setText(_translate("Dialog", "3"))
        self.pushButton_4.setText(_translate("Dialog", "4"))
        self.pushButton_5.setText(_translate("Dialog", "5"))
        self.pushButton_6.setText(_translate("Dialog", "6"))
        self.pushButton_7.setText(_translate("Dialog", "7"))
        self.pushButton_8.setText(_translate("Dialog", "8"))
        self.pushButton_9.setText(_translate("Dialog", "9"))
        self.pushButton_0.setText(_translate("Dialog", "0"))
        self.pushButton_dot.setText(_translate("Dialog", "."))
        self.pushButton_equ.setText(_translate("Dialog", "="))
        self.pushButton_div.setText(_translate("Dialog", "/"))
        self.pushButton_mul.setText(_translate("Dialog", "*"))
        self.pushButton_add.setText(_translate("Dialog", "+"))
        self.pushButton_sub.setText(_translate("Dialog", "-"))
        self.pushButton_cls.setText(_translate("Dialog", "cls"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

