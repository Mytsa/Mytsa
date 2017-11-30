# -*- coding: utf-8 -*-
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

# app = QApplication(sys.argv)
#
# window = QWidget()
# window.setGeometry(100, 100, 300, 300)
# window.setWindowTitle('calculation of cycles')
#
# window.show()
# sys.exit(app.exec())


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('calculation of cycles')
        # self.setWindowIcon(QGui.QIcon('namefile.png'))  # add image in window
        self.show()

app = QApplication(sys.argv)
Gui = Window()
sys.exit(app.exec_())

import sys
# Импортируем наш интерфейс из файла
from vash_ui import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку
        self.ui.pushButton.clicked.connect(self.MyFunction)

    # Пока пустая функция которая выполняется
    # при нажатии на кнопку
    def MyFunction(self):
        pass

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())