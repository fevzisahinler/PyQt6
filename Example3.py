
from PyQt6 import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class guiapp(QDialog):
    def __init__(self,parent=None):
        super(guiapp,self).__init__(parent)

        self.label = QLabel("Basilmadan Once")

        btn = QPushButton("Buton")
        btn.clicked.connect(self.tikla)

        box = QVBoxLayout()
        box.addWidget(btn)
        box.addWidget(self.label)

        self.setLayout(box)
        self.setWindowTitle("Mert")
        self.move(69,59)
        self.resize(13,123)


    def tikla(self):
        self.label.setText("Tiklandi")

app = QApplication([])
win = guiapp()

win.show()
app.exec()