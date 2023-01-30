from PyQt6 import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class guiUygulama3 (QDialog):
    def __init__(self, parent=None):
        super(guiUygulama3,self).__init__(parent)
        self.boy = 2
        self.yt = {0:'Arial', 1:'Times New Roman', 2:'Verdana', 3:'Comic Sans MS'}
        self.yaziTipi = self.yt[0]
        self.metin = '<center><font color ="blue" size ="+%d" face="%s"> görsel programlama dersi</font></center>'
        self.etiket = QLabel(self.metin % (self.boy, self.yaziTipi))
        izgara = QGridLayout()
        izgara.addWidget(self.etiket, 0, 0, 1, 2)
        izgara.addWidget(QLabel('Yazı Boyu: '), 1,0,1,1)
        donerKutu = QSpinBox()
        donerKutu.setRange(1, 4)
        donerKutu.setValue(self.boy)
        donerKutu.valueChanged.connect(self.metinBoyuDegistir)
        izgara.addWidget(donerKutu,1,1,1,1)
        izgara.addWidget(QLabel('Yazı Tipi: '), 2,0,1,1)
        acilirListe = QComboBox()
        acilirListe.addItem('Arial')
        acilirListe.addItem('Times New Roman')
        acilirListe.addItem('Verdana')
        acilirListe.addItem('Comic Sans MS')
        listeMetinIndisi = acilirListe.findText(self.yaziTipi)
        acilirListe.setCurrentIndex(listeMetinIndisi)
        acilirListe.activated.connect(self.yaziTipiDegistir)  #.connect(self.yazıTipiDegistir) #.connect   #.connect(self.yazıTipiDegistir)
        izgara.addWidget(acilirListe, 2,1,1,1)
        self.setLayout(izgara)
        self.setWindowTitle("Metin Formatı")
        self.resize(500,150)
        
        
    
    def metinBoyuDegistir (self, boy):
        self.boy = boy 
        self.etiket.setText(self.metin % (self.boy, self.yaziTipi))
                           
    def yaziTipiDegistir (self, tip):
        self.yaziTipi = self.yt[tip]
        self.etiket.setText(self.metin % (self.boy,self.yaziTipi))
        
                
                      
uyg = QApplication([])
pencere = guiUygulama3()  
pencere.show()
uyg.exec()     
        