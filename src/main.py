import sys

from PyQt5.QtWidgets import QApplication

from gui.window import PAPWindow

app = QApplication(sys.argv)
w = PAPWindow()
w.show()
app.exec()
