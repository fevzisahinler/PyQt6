from PyQt6 import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class yaziTipiDiyalog (QDialog):
    def __init__(self, parent=None):
        super(yaziTipiDiyalog,self).__init__(parent)
        izgara = QGridLayout()
        # widgetlar tek tek eklenir. Diyalog örneği için yüklenen jpgyi inceleyiniz
        izgara.addWidget(QLabel ('Yazı Tipi:'),0,0,1,1)
        self.yaziTipiListe= QComboBox()
        self.yaziTipiListe.addItems(('Arial','Times New Roman', 'Verdana', 'Comic Sans MS'))
        self.yaziTipiListe.setCurrentIndex(2)
        izgara.addWidget(self.yaziTipiListe,0,1,1,1)
        
        kabulDugme = QPushButton("Tamam")
        iptalDugme = QPushButton("İptal")
        kabulDugme.setDefault(True) # kabulDugme ön tanımlı yapıldı. Şart değil.
        
        dugmeKutusu = QHBoxLayout()
        dugmeKutusu.addWidget(kabulDugme)
        dugmeKutusu.addWidget(iptalDugme)
        izgara.addLayout(dugmeKutusu, 1,0,1,2)
        
        kabulDugme.clicked.connect(self.accept)
        iptalDugme.clicked.connect(self.reject)
        
        self.setLayout(izgara)
        self.resize(300, 100)
        
        self.setWindowTitle("YazıTipi Ayarı")
        self.setWindowIcon(QIcon("icons8-spyder-ide-5-48.png"))
        
        
        
class AnaUygulamaAkılsızDiyalog (QDialog):
    def __init__(self, parent=None):
        super(AnaUygulamaAkılsızDiyalog,self).__init__(parent)
        self.yaziTipi = 'Verdana'
        self.metin = '<font color ="black" face="%s" size ="+3"> görsel programlama dersi</font>'
        self.etiket = QLabel(self.metin % self.yaziTipi)
        kutu = QVBoxLayout()
        kutu.addWidget(self.etiket)
        
        yaziTipiDugme = QPushButton("Yazı Tipini Değiştir")
        yaziTipiDugme.clicked.connect(self.yaziTipiDegistir)
        kutu.addWidget(yaziTipiDugme)
        self.setLayout(kutu)
        self.setWindowTitle("Ana Uygulama")
        self.setWindowIcon(QIcon("icons8-python-50"))
    
    def yaziTipiDegistir(self):
        diyalog = yaziTipiDiyalog()
        if diyalog.exec():
            self.yaziTipi= diyalog.yaziTipiListe.currentText()
            self.etiket.setText(self.metin % self.yaziTipi)
            
            
        
uyg = QApplication([]) 
pencere = AnaUygulamaAkılsızDiyalog() 
pencere.show()
uyg.exec()        