from PyQt6 import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class guiUygulama2 (QDialog):
    def __init__(self, parent=None):
        super(guiUygulama2,self).__init__(parent)
        self.height = 3
        self.text = '<center><font color ="blue" size ="+%d"> görsel programlama dersi</font></center>'
        self.label = QLabel(self.text % self.height)
        buttonkucult = QPushButton('Metni Küçült')
        buttonkucult.clicked.connect(self.metinKucult)
        buttonbuyut= QPushButton("Metni Büyüt")
        buttonbuyut.clicked.connect(self.metinBuyut)
        grid = QGridLayout()
        grid.addWidget(self.label, 0,0,1,2)
        grid.addWidget(buttonkucult,1,0,1,1)
        grid.addWidget(buttonbuyut,1,1,1,1)

        self.setLayout(grid)
        self.setWindowTitle('PyQt Izgarasi')
        self.resize(500, 100)
    
    def metinBuyut (self):
        if self.height <=4:
            self.heigh = self.height + 1
            self.label.setText(self.text % self.height) 
            print (self.height)
            
    def metinKucult(self):
        if self.height >= 1:
            self.height = self.height - 1
            self.label.setText(self.text % self.height) 
            print (self.height)
        
        
uyg = QApplication([])     
pencere = guiUygulama2()
pencere.show()
uyg.exec()