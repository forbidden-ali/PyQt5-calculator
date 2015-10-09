# -*- coding: utf-8 -*-

"""
Module implementing calculate.
"""
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog,  QApplication

from Ui_calculator import Ui_Dialog


class calculate(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(calculate, self).__init__(parent)
        self.setupUi(self)
        
        self.flag = 0
        self.flag_flag = ''
        self.num_1 = '0'
        self.num_2 = '0'
        self.num_3 = '0'
    
    @pyqtSlot()
    def on_pushButton_1_clicked(self):
        if self.flag == 0:
            if self.num_1 == '0':
                self.num_1 = '1'
                self.lcd.display(self.num_1)
            else:
                self.num_1 = self.num_1+'1'
                self.lcd.display(self.num_1)
        else:
            if self.num_2 == '0':
                self.num_2 = '1'
                self.lcd.display(self.num_2)
            else:
                self.num_2 = self.num_2 + '1'
                self.lcd.display(self.num_2)
            
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        if self.flag == 0:
            if self.num_1 == '0':
                self.num_1 = '2'
                self.lcd.display(self.num_1)
            else:
                self.num_1 = self.num_1+'2'
                self.lcd.display(self.num_1)
        else:
            if self.num_2 == '0':
                self.num_2 = '2'
                self.lcd.display(self.num_2)
            else:
                self.num_2 = self.num_2 + '2'
                self.lcd.display(self.num_2)
    
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        if self.flag == 0:
            if self.num_1 == '0':
                self.num_1 = '3'
                self.lcd.display(self.num_1)
            else:
                self.num_1 = self.num_1+'3'
                self.lcd.display(self.num_1)
        else:
            if self.num_2 == '0':
                self.num_2 = '3'
                self.lcd.display(self.num_2)
            else:
                self.num_2 = self.num_2 + '3'
                self.lcd.display(self.num_2)
    
    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        if self.flag == 0:
            if self.num_1 == '0':
                self.num_1 = '4'
                self.lcd.display(self.num_1)
            else:
                self.num_1 = self.num_1+'4'
                self.lcd.display(self.num_1)
        else:
            if self.num_2 == '0':
                self.num_2 = '4'
                self.lcd.display(self.num_2)
            else:
                self.num_2 = self.num_2 + '4'
                self.lcd.display(self.num_2)
    
    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        if self.flag == 0:
            if self.num_1 == '0':
                self.num_1 = '5'
                self.lcd.display(self.num_1)
            else:
                self.num_1 = self.num_1+'5'
                self.lcd.display(self.num_1)
        else:
            if self.num_2 == '0':
                self.num_2 = '5'
                self.lcd.display(self.num_2)
            else:
                self.num_2 = self.num_2 + '5'
                self.lcd.display(self.num_2)
    
    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        if self.flag == 0:
            if self.num_1 == '0':
                self.num_1 = '6'
                self.lcd.display(self.num_1)
            else:
                self.num_1 = self.num_1+'6'
                self.lcd.display(self.num_1)
        else:
            if self.num_2 == '0':
                self.num_2 = '6'
                self.lcd.display(self.num_2)
            else:
                self.num_2 = self.num_2 + '6'
                self.lcd.display(self.num_2)
    
    @pyqtSlot()
    def on_pushButton_7_clicked(self):
        if self.flag == 0:
            if self.num_1 == '0':
                self.num_1 = '7'
                self.lcd.display(self.num_1)
            else:
                self.num_1 = self.num_1+'7'
                self.lcd.display(self.num_1)
        else:
            if self.num_2 == '0':
                self.num_2 = '7'
                self.lcd.display(self.num_2)
            else:
                self.num_2 = self.num_2 + '7'
                self.lcd.display(self.num_2)
    
    @pyqtSlot()
    def on_pushButton_8_clicked(self):
        if self.flag == 0:
            if self.num_1 == '0':
                self.num_1 = '8'
                self.lcd.display(self.num_1)
            else:
                self.num_1 = self.num_1+'8'
                self.lcd.display(self.num_1)
        else:
            if self.num_2 == '0':
                self.num_2 = '8'
                self.lcd.display(self.num_2)
            else:
                self.num_2 = self.num_2 + '8'
                self.lcd.display(self.num_2)
    
    @pyqtSlot()
    def on_pushButton_9_clicked(self):
        if self.flag == 0:
            if self.num_1 == '0':
                self.num_1 = '9'
                self.lcd.display(self.num_1)
            else:
                self.num_1 = self.num_1+'9'
                self.lcd.display(self.num_1)
        else:
            if self.num_2 == '0':
                self.num_2 = '9'
                self.lcd.display(self.num_2)
            else:
                self.num_2 = self.num_2 + '9'
                self.lcd.display(self.num_2)
    
    @pyqtSlot()
    def on_pushButton_0_clicked(self):
        if self.flag == 0:
            if self.num_1 == '0':
                self.num_1 = '0'
                self.lcd.display(self.num_1)
            else:
                self.num_1 = self.num_1+'0'
                self.lcd.display(self.num_1)
        else:
            if self.num_2 == '0':
                self.num_2 = '0'
                self.lcd.display(self.num_2)
            else:
                self.num_2 = self.num_2 + '0'
                self.lcd.display(self.num_2)
    
    @pyqtSlot()
    def on_pushButton_dot_clicked(self):
        if self.flag == 0:
            if self.num_1 == '0':
                self.num_1 = '0.'
                self.lcd.display(self.num_1)
            else:
                self.num_1 = self.num_1+'.'
                self.lcd.display(self.num_1)
        else:
            if self.num_2 == '0':
                self.num_2 = '0.'
                self.lcd.display(self.num_2)
            else:
                self.num_2 = self.num_2 + '.'
                self.lcd.display(self.num_2)
    
    @pyqtSlot()    
    def on_pushButton_equ_clicked(self):
        if self.flag == 1:
            if self.flag_flag == '+':
                self.num_3 = str(float(self.num_1) + float(self.num_2))
                self.lcd.display(self.num_3)
                self.flag = 0
                self.num_1 = '0'
                self.num_2 = '0'
                self.num_3 = '0'
            
            elif self.flag_flag == '-':
                self.num_3 = str(float(self.num_1) - float(self.num_2))
                self.lcd.display(self.num_3)
                self.flag = 0
                self.num_1 = '0'
                self.num_2 = '0'
                self.num_3 = '0'
                
            elif self.flag_flag == '*':
                self.num_3 = str(float(self.num_1) * float(self.num_2))
                self.lcd.display(self.num_3)
                self.flag = 0
                self.num_1 = '0'
                self.num_2 = '0'
                self.num_3 = '0'
            
            elif self.flag_flag == '/':
                self.num_3 = str(float(self.num_1) / float(self.num_2))
                self.lcd.display(self.num_3)
                self.flag = 0
                self.num_1 = '0'
                self.num_2 = '0'
                self.num_3 = '0'
            else:
                pass
            
    @pyqtSlot()
    def on_pushButton_div_clicked(self):
        self.flag = 1
        self.flag_flag = '/'
        self.lcd.display(0)
    
    @pyqtSlot()
    def on_pushButton_mul_clicked(self):
        self.flag = 1
        self.flag_flag = '*'
        self.lcd.display(0)
    
    @pyqtSlot()
    def on_pushButton_add_clicked(self):
        self.flag = 1
        self.flag_flag = '+'
        self.lcd.display(0)
    
    @pyqtSlot()
    def on_pushButton_sub_clicked(self):
        self.flag = 1
        self.flag_flag = '-'
        self.lcd.display(0)
            
    
    @pyqtSlot()
    def on_pushButton_cls_clicked(self):
        self.num_1 = '0'
        self.num_2 = '0'
        self.flag = 0
        self.flag_flag = ''
        self.lcd.display(self.num_1) 
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculate = calculate()
    calculate.show()
    sys.exit(app.exec_())
