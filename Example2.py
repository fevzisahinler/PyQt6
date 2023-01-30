from PyQt6 import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


def bas():
   label.setText("Fevzi")

app = QApplication([])
win = QWidget()

label = QLabel("Mert Karatay")
btn = QPushButton("Click me")
btn.clicked.connect(bas)

box = QVBoxLayout()
box.addWidget(label)
box.addWidget(btn)

win.setLayout(box)
win.setWindowTitle("Mert Karatay")

win.show()
app.exec()