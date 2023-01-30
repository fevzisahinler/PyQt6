
from PyQt6 import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

# * Example1 * #


app = QApplication([])
win = QWidget()

Label = QLabel("Pushlabel Box")
Button = QPushButton("Click me")

Box = QVBoxLayout()
Box.addWidget(Label)
Box.addWidget(Button)

win.setLayout(Box)
win.setWindowTitle("Tiklanabilir Buton")

win.show()
app.exec()