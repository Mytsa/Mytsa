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
