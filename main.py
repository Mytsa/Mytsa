# -*- coding: utf-8 -*-
import sys
from openpyxl import *
from datetime import datetime
from gui import *    # gui is interface file
from f_w_r import *



from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.date = datetime.strftime(datetime.now(), "%d/%m/%Y")
        self.time = datetime.strftime(datetime.now(), "%H:%M")
        self.w_date = datetime.strftime(datetime.now(), "%W")
        self.m_date = datetime.strftime(datetime.now(), "%m")

        # Здесь прописываем событие нажатия на кнопку
        self.ui.pushButton.clicked.connect(self.Add)
        # self.ui.pushButton1.clicked.connect(self.MyFunction1)
        # self.ui.pushButton2.clicked.connect(self.MyFunction2)
        # self.ui.pushButton3.clicked.connect(self.MyFunction3)
        # self.ui.pushButton4.clicked.connect(self.MyFunction4)
        # self.ui.pushButton5.clicked.connect(self.MyFunction5)
        # self.ui.pushButton6.clicked.connect(self.MyFunction6)
        # self.ui.pushButton7.clicked.connect(self.MyFunction7)

    # Пока пустая функция которая выполняется
    # при нажатии на кнопку
    def Add(self):
        eq_number = self.ui.eq_number.toPlainText()  # input equipment number
        per_number = self.ui.per_number.toPlainText()  # input personal number

        minutes = self.ui.minutes.toPlainText()  # input minutes
        notice = self.ui.notice.toPlainText()  # input notice
        # print(eq_number + str(' eq_num') + per_number + str(' per num'), notice + str(' commet'), minutes + str(' minutes'))


        name = eq_number
        sheet = 'main'
        mark = 'Gamma 1 (8_1235)'
        mes = str(find_row(name, sheet, mark))
        print(mes)
        message = self.ui.message.setText(mes)  # output message/status of run
        print(message)





    def MyFunction1(self):
        pass

    def MyFunction2(self):
        pass

    def MyFunction3(self):
        pass

    def MyFunction4(self):
        pass

    def MyFunction5(self):
        pass

    def MyFunction6(self):
        pass

    def MyFunction7(self):
        pass




if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
