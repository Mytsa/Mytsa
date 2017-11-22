import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setGeometry(100, 100, 300, 300)
window.setWindowTitle('calculation of cycles')

window.show()
sys.exit(app.exec())
