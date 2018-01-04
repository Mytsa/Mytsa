# -*- coding: utf-8 -*-
import sys
# window1 is our interface file
from gui import *
from message_spare_parts import *

class MyWin(QtWidgets.QDialog, Message):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.mes = Message()

        self.ui.pushButton.clicked.connect(self.action)  # calculation


    def action(self):
        # output clean area
        self.ui.counter.setText("")  # counter


        # input data
        per_number = self.ui.per_number.toPlainText()     # input personal number
        counter = self.ui.counter.toPlainText()  # input counter

        # calculation logica


        # output data
        self.ui.counter.setText(counter)


        # read/write data intro/to file
        self.mes.write(per_number, defect, sap_eq, type_eq, fault, counter)
        self.mes.print_mes(file_name)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
sys.exit(app.exec_())
