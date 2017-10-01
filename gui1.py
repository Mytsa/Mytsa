import sys
from PyQt5.QtWidgets import QApplication, QWidget


app = QApplication(sys.argv)

w = QWidget()
w.resize(250, 150)
w.setWindowTitle('herna vsaka')
w.show()

sys.exit(app.exec_())